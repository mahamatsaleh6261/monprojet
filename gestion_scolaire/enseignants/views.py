from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime

from comptes.models import Compte, get_country_code
from staffs.views import is_staff, is_not_anonymous, is_enseignant
from cours.models import Attribution
from notes.models import Evaluation, Note
from etudiants.models import Inscription

from .models import Enseignant
from .forms import EnseignantCreationForm, EnseignantUpdateForm


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
@transaction.atomic
def enseignant_create_view(request):
    if request.method == "POST":
        form = EnseignantCreationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            sexe = form.cleaned_data["sexe"]
            telephone = form.cleaned_data["telephone"]
            email = form.cleaned_data["email"]
            # type_de_compte = form.cleaned_data['type_de_compte']
            # photo = form.cleaned_data['photo']

            compte = Compte.objects.create_user(
                email=email,
                telephone=telephone,
                password="1234",
                type_de_compte="EN",
            )

            enseignant = Enseignant.objects.create(
                compte=compte, nom=nom, prenom=prenom, sexe=sexe
            )

            return redirect("enseignants:enseignants")

    form = EnseignantCreationForm()
    return render(request, "enseignants/enseignant_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
@transaction.atomic
def enseignant_list_view(request):
    queryset = Enseignant.objects.all()

    if request.method == "POST":
        compte = Compte()
        enseignant = Enseignant()
        form = EnseignantCreationForm(request.POST, request.FILES)
        if form.is_valid():
            compte.telephone = form.cleaned_data["telephone"]
            compte.email = form.cleaned_data["email"]
            compte.photo = request.FILES["photo"]
            compte.type_de_compte = "EN"
            compte.set_password("1234")
            compte.save()

            enseignant.compte = compte
            enseignant.nom = form.cleaned_data["nom"]
            enseignant.prenom = form.cleaned_data["prenom"]
            enseignant.sexe = form.cleaned_data["sexe"]
            enseignant.date_de_naissance = form.cleaned_data["date_de_naissance"]
            enseignant.pays = form.cleaned_data["pays"]

            annee_de_naissance = datetime.strptime(
                enseignant.date_de_naissance, "%d/%m/%Y"
            ).year

            enseignant.matricule = (
                "EN"
                + "{:04d}".format(enseignant.compte.pk)
                + enseignant.sexe
                + str(annee_de_naissance)
                + get_country_code(enseignant.pays)
            )

            enseignant.save()

            return redirect("enseignants:enseignants")

    form = EnseignantCreationForm()
    context = {"enseignants": queryset, "form": form}
    return render(request, "enseignants/enseignant_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def enseignant_detail_view(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    matieres = Attribution.objects.filter(enseignant=enseignant)

    context = {"enseignant": enseignant, "programmes": matieres}
    return render(request, "enseignants/enseignant_detail.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def enseignant_matiere_list_view(request):
    enseignant = get_object_or_404(Enseignant, pk=request.user.pk)
    matieres = Attribution.objects.filter(enseignant=enseignant)

    context = {"enseignant": enseignant, "programmes": matieres}
    return render(request, "cours/matiere_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def enseignant_update_view(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    attributions = Attribution.objects.filter()

    form = EnseignantUpdateForm(
        initial={
            "nom": enseignant.nom,
            "prenom": enseignant.prenom,
            "date_de_naissance": enseignant.date_de_naissance,
            "sexe": enseignant.sexe,
            "pays": enseignant.pays,
            "telephone": enseignant.compte.telephone,
        }
    )

    if request.method == "POST":
        form = EnseignantUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            compte = enseignant.compte
            compte.telephone = form.cleaned_data["telephone"]
            compte.photo = request.FILES["photo"]
            compte.save()

            enseignant.nom = form.cleaned_data["nom"]
            enseignant.prenom = form.cleaned_data["prenom"]
            enseignant.sexe = form.cleaned_data["sexe"]
            enseignant.date_de_naissance = form.cleaned_data["date_de_naissance"]
            enseignant.pays = form.cleaned_data["pays"]

            annee = datetime.strptime(enseignant.date_de_naissance, "%d/%m/%Y").year

            enseignant.matricule = (
                "EN"
                + "{:04d}".format(enseignant.compte.pk)
                + enseignant.sexe
                + str(annee)
                + get_country_code(enseignant.pays)
            )

            enseignant.save()

            return redirect("enseignants:enseignant", enseignant.pk)

    context = {"enseignant": enseignant, "programmes": attributions, "form": form}
    return render(request, "enseignants/enseignant_detail.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def enseignant_dashboard_view(request):
    queryset = Enseignant.objects.all()
    context = {"enseignant": queryset}
    return render(request, "enseignants/dashboard.html", context)
