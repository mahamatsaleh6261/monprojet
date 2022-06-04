from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime

from comptes.models import Compte, get_country_code

from .models import Staff
from .forms import StaffCreationForm


def is_admin(user):
    return user.type_de_compte == "AD"


def is_staff(user):
    return user.type_de_compte == "ST"


def is_enseignant(user):
    return user.type_de_compte == "EN"


def is_etudiant(user):
    return user.type_de_compte == "ET"


def is_authorised(user):
    return user.type_de_compte == "AD" or user.type_de_compte == "ST"


def is_not_anonymous(user):
    return user.is_anonymous == False


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_admin, login_url="/")
@login_required(login_url="/")
@transaction.atomic
def staff_create_view(request):

    if request.method == "POST":
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
        form = StaffCreationForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            sexe = form.cleaned_data["sexe"]
            telephone = form.cleaned_data["telephone"]
            email = form.cleaned_data["email"]
            type_de_compte = form.cleaned_data["type_de_compte"]
            # photo = form.cleaned_data['photo']

            compte = Compte.objects.create_user(
                email=email,
                telephone=telephone,
                password="1234",
                type_de_compte=type_de_compte,
            )

            staff = Staff.objects.create(
                compte=compte, nom=nom, prenom=prenom, sexe=sexe
            )

            return redirect("staffs:staffs")

    form = StaffCreationForm()
    return render(request, "staffs/staff_creation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_authorised, login_url="/")
@login_required(login_url="/")
def staff_dashboard_view(request):
    return render(request, "staffs/staff_dashboard.html", {})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_admin, login_url="/")
@login_required(login_url="/")
@transaction.atomic
def staff_list_view(request):
    queryset = Staff.objects.all()

    if request.method == "POST":
        compte = Compte()
        staff = Staff()
        form = StaffCreationForm(request.POST, request.FILES)
        if form.is_valid():
            compte.telephone = form.cleaned_data["telephone"]
            compte.email = form.cleaned_data["email"]
            compte.photo = request.FILES["photo"]
            compte.type_de_compte = form.cleaned_data["type_de_compte"]
            compte.set_password("1234")
            compte.save()

            staff.compte = compte
            staff.nom = form.cleaned_data["nom"]
            staff.prenom = form.cleaned_data["prenom"]
            staff.sexe = form.cleaned_data["sexe"]
            staff.date_de_naissance = form.cleaned_data["date_de_naissance"]
            staff.pays = form.cleaned_data["pays"]

            annee_de_naissance = datetime.strptime(
                staff.date_de_naissance, "%d/%m/%Y"
            ).year

            staff.matricule = (
                staff.compte.type_de_compte
                + "{:04d}".format(staff.compte.pk)
                + staff.sexe
                + str(annee_de_naissance)
                + get_country_code(staff.pays)
            )

            staff.save()

            return redirect("staffs:staffs")

    form = StaffCreationForm()
    context = {"staffs": queryset, "form": form}
    return render(request, "staffs/staff_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_admin, login_url="/")
@login_required(login_url="/")
def staff_detail_view(request, pk):
    staff = get_object_or_404(Staff, pk=pk)

    context = {"staff": staff}
    return render(request, "staffs/staff_detail.html", context)
