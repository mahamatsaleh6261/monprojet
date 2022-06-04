from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from staffs.views import is_staff, is_not_anonymous, is_enseignant
from enseignants.models import Enseignant

from .forms import ModuleCreationForm, MatiereCreationForm, ProgrammeCreationForm
from .models import Module, Matiere, Attribution


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def create_module(request):
    if request.method == "POST":
        form = ModuleCreationForm(request.POST)

        if form.is_valid():
            specialite = form.cleaned_data["specialite"]
            grade = form.cleaned_data["grade"]
            semestre = form.cleaned_data["semestre"]
            code = form.cleaned_data["code"]
            nom = form.cleaned_data["nom"]

            Module.objects.create(
                specialite=specialite,
                grade=grade,
                semestre=semestre,
                code=code,
                nom=nom,
            )

            return redirect("cours:modules")

    form = ModuleCreationForm()
    return render(request, "cours/module_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def create_matiere(request):
    if request.method == "POST":
        form = MatiereCreationForm(request.POST)

        if form.is_valid():
            module = form.cleaned_data["module"]
            code = form.cleaned_data["code"]
            nom = form.cleaned_data["nom"]
            credit = form.cleaned_data["credit"]

            Matiere.objects.create(module=module, code=code, nom=nom, credit=credit)

            return redirect("cours:matieres")

    form = MatiereCreationForm()
    return render(request, "cours/matiere_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def module_list_view(request):
    queryset = Module.objects.all()

    if request.method == "POST":
        form = ModuleCreationForm(request.POST)

        if form.is_valid():
            specialite = form.cleaned_data["specialite"]
            semestre = form.cleaned_data["semestre"]
            grade = form.cleaned_data["grade"]
            code = form.cleaned_data["code"]
            nom = form.cleaned_data["nom"]

            Module.objects.create(
                specialite=specialite,
                semestre=semestre,
                grade=grade,
                code=code,
                nom=nom,
            )

            return redirect("cours:modules")

    form = ModuleCreationForm()
    context = {"modules": queryset, "form": form}
    return render(request, "cours/module_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def matiere_list_view(request):
    queryset = Matiere.objects.all()

    if request.method == "POST":
        form = MatiereCreationForm(request.POST)

        if form.is_valid():
            module = form.cleaned_data["module"]
            code = form.cleaned_data["code"]
            nom = form.cleaned_data["nom"]
            credit = form.cleaned_data["credit"]

            Matiere.objects.create(module=module, code=code, nom=nom, credit=credit)

            return redirect("cours:matieres")

    form = MatiereCreationForm()
    context = {"matieres": queryset, "form": form}
    return render(request, "cours/matiere_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def enseignant_matiere_list_view(request):
    enseignant = get_object_or_404(Enseignant, pk=request.user.pk)
    matieres = Attribution.objects.filter(enseignant=enseignant)

    context = {"enseignant": enseignant, "matieres": matieres}
    return render(request, "cours/matiere_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def matiere_view(request):
    queryset = Matiere.objects.all()

    # if request.method == "POST":
    #     form = MatiereCreationForm(request.POST)

    #     if form.is_valid():
    #         module = form.cleaned_data["module"]
    #         code = form.cleaned_data["code"]
    #         nom = form.cleaned_data["nom"]
    #         credit = form.cleaned_data["credit"]

    #         Matiere.objects.create(module=module, code=code, nom=nom, credit=credit)

    #         return redirect("cours:matieres")

    # form = MatiereCreationForm()
    context = {"matieres": queryset}
    return render(request, "cours/dashboard.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def cours_dashboard_view(request):
    modules = Module.objects.all()
    matieres = Matiere.objects.all()
    context = {"modules": modules, "matieres": matieres}
    return render(request, "cours/dashboard.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def matiere_detail_view(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)

    if request.method == "POST":
        form = ProgrammeCreationForm(request.POST)

        if form.is_valid():
            enseignant = form.cleaned_data["enseignant"]
            annee = form.cleaned_data["annee"]

            if not Attribution.objects.filter(
                enseignant=enseignant, matiere=matiere, annee=annee
            ).exists():
                Attribution.objects.create(
                    enseignant=enseignant, matiere=matiere, annee=annee
                )

            return redirect("cours:matieres")

    form = ProgrammeCreationForm()
    context = {"matiere": matiere, "form": form}
    return render(request, "cours/matiere_detail.html", context)
