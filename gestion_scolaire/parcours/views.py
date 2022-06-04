from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from staffs.views import is_staff, is_not_anonymous
from .forms import DomainCreationForm, MentionCreationForm, SpecialiteCreationForm
from .models import Domain, Mention, Specialite


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def create_domain(request):
    if request.method == "POST":
        form = DomainCreationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]

            domain = Domain.objects.create(nom=nom)

            return redirect("parcours:domains")

    form = DomainCreationForm()
    return render(request, "parcours/domain_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def create_mention(request):
    if request.method == "POST":
        form = MentionCreationForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"]
            nom = form.cleaned_data["nom"]

            Mention.objects.create(domain=domain, nom=nom)

            return redirect("parcours:mentions")

    form = MentionCreationForm()
    return render(request, "parcours/mention_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def create_specialite(request):
    if request.method == "POST":
        form = SpecialiteCreationForm(request.POST)
        if form.is_valid():
            mention = form.cleaned_data["mention"]
            nom = form.cleaned_data["nom"]
            sigle = form.cleaned_data["sigle"]

            Specialite.objects.create(mention=mention, nom=nom, sigle=sigle)

            return redirect("parcours:specialites")

    form = SpecialiteCreationForm()
    return render(request, "parcours/specialite_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def domain_list_view(request):
    queryset = Domain.objects.all()

    if request.method == "POST":
        form = DomainCreationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]

            domain = Domain.objects.create(nom=nom)

            return redirect("parcours:domains")

    form = DomainCreationForm()
    context = {"domains": queryset, "form": form}
    return render(request, "parcours/domain_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def mention_list_view(request):
    queryset = Mention.objects.all()

    if request.method == "POST":
        form = MentionCreationForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"]
            nom = form.cleaned_data["nom"]

            Mention.objects.create(domain=domain, nom=nom)

            return redirect("parcours:mentions")

    form = MentionCreationForm()
    context = {"mentions": queryset, "form": form}
    return render(request, "parcours/mention_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def specialite_list_view(request):
    queryset = Specialite.objects.all()

    if request.method == "POST":
        form = SpecialiteCreationForm(request.POST)
        if form.is_valid():
            mention = form.cleaned_data["mention"]
            nom = form.cleaned_data["nom"]
            sigle = form.cleaned_data["sigle"]

            Specialite.objects.create(mention=mention, nom=nom, sigle=sigle)

            return redirect("parcours:specialites")

    form = SpecialiteCreationForm()
    context = {"specialites": queryset, "form": form}
    return render(request, "parcours/specialite_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def dashboard_view(request):
    queryset = Specialite.objects.all()
    context = {"specialites": queryset}

    return render(request, "parcours/dashboard.html", context)
