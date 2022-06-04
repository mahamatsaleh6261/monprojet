from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime

from comptes.models import Compte, get_country_code
from staffs.views import is_staff, is_not_anonymous, is_etudiant
from parcours.models import Specialite
from cours.models import Module, Matiere
from notes.models import Note

from .models import Etudiant, Inscription
from .forms import EtudiantCreationForm, InscriptionForm, EtudiantUpdateForm


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def etudiant_list_view(request):
    etudiants = Etudiant.objects.all()

    if request.method == "POST":
        compte = Compte()
        etudiant = Etudiant()

        form = EtudiantCreationForm(request.POST, request.FILES)

        if form.is_valid():
            compte.telephone = form.cleaned_data["telephone"]
            compte.email = form.cleaned_data["email"]
            compte.photo = request.FILES["photo"]
            compte.type_de_compte = "ET"
            compte.save()

            etudiant.compte = compte
            etudiant.nom = form.cleaned_data["nom"]
            etudiant.prenom = form.cleaned_data["prenom"]
            etudiant.sexe = form.cleaned_data["sexe"]
            etudiant.date_de_naissance = form.cleaned_data["date_de_naissance"]
            etudiant.pays = form.cleaned_data["pays"]
            etudiant.groupe_sanguin = form.cleaned_data["groupe_sanguin"]

            etudiant.matricule = (
                "ET"
                + "{:04d}".format(etudiant.compte.pk)
                + etudiant.sexe
                + str(datetime.strptime(etudiant.date_de_naissance, "%d/%m/%Y").year)
                + get_country_code(etudiant.pays)
            )

            etudiant.save()

            return redirect("etudiants:etudiants")

    form = EtudiantCreationForm()
    context = {"etudiants": etudiants, "form": form}
    return render(request, "etudiants/etudiant_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def etudiant_detail_view(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    details = Inscription.objects.filter(etudiant=etudiant).order_by("-grade")
    matieres = []

    if details is not None:
        for detail in details:
            modules = Module.objects.filter(
                specialite=detail.specialite, grade=detail.grade
            )
            for module in modules:
                for matiere in Matiere.objects.filter(module=module):
                    if matiere is not None:
                        matieres.append(matiere)

    context = {"etudiant": etudiant, "details": details, "matieres": matieres}
    return render(request, "etudiants/etudiant_detail.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_etudiant, login_url="/")
@login_required(login_url="/")
def etudiant_matiere_view(request):
    etudiant = get_object_or_404(Etudiant, pk=request.user.id)
    details = Inscription.objects.filter(etudiant=etudiant).order_by("-grade")
    matieres = []

    if details is not None:
        for detail in details:
            modules = Module.objects.filter(
                specialite=detail.specialite, grade=detail.grade
            )
            for module in modules:
                for matiere in Matiere.objects.filter(module=module):
                    if matiere is not None:
                        matieres.append(matiere)

    context = {"etudiant": etudiant, "details": details, "matieres": matieres}
    return render(request, "etudiants/etudiant_matiere_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_etudiant, login_url="/")
@login_required(login_url="/")
def etudiant_note_view(request):
    etudiant = get_object_or_404(Etudiant, pk=request.user.id)

    context = {"etudiant": etudiant}
    return render(request, "etudiants/etudiant_note_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def etudiant_inscription_view(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    details = Inscription.objects.filter(etudiant=etudiant).order_by("-grade")
    matieres = []

    if request.method == "POST":
        inscription = Inscription()
        specialite = Specialite()

        form = InscriptionForm(request.POST)

        if form.is_valid():
            specialite = form.cleaned_data["specialite"]
            grade = form.cleaned_data["grade"]
            annee = form.cleaned_data["annee"]

            if not Inscription.objects.filter(
                etudiant=etudiant, specialite=specialite, grade=grade, annee=annee
            ).exists():
                inscription.etudiant = etudiant
                inscription.specialite = specialite
                inscription.grade = grade
                inscription.annee = annee
                inscription.save()

            return redirect("etudiants:etudiant", etudiant.pk)

    if details is not None:
        for detail in details:
            modules = Module.objects.filter(
                specialite=detail.specialite, grade=detail.grade
            )
            for module in modules:
                for matiere in Matiere.objects.filter(module=module):
                    if matiere is not None:
                        matieres.append(matiere)

    form = InscriptionForm()
    context = {
        "etudiant": etudiant,
        "details": details,
        "matieres": matieres,
        "form": form,
    }
    return render(request, "etudiants/etudiant_detail.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_staff, login_url="/")
@login_required(login_url="/")
def etudiant_update_view(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    details = Inscription.objects.filter(etudiant=etudiant).order_by("-grade")
    matieres = []

    form = EtudiantUpdateForm(
        initial={
            "nom": etudiant.nom,
            "prenom": etudiant.prenom,
            "date_de_naissance": etudiant.date_de_naissance,
            "sexe": etudiant.sexe,
            "pays": etudiant.pays,
            "groupe_sanguin": etudiant.groupe_sanguin,
            "telephone": etudiant.compte.telephone,
            "photo": etudiant.compte.telephone,
        }
    )

    if request.method == "POST":
        form = EtudiantUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            compte = etudiant.compte
            compte.telephone = form.cleaned_data["telephone"]
            compte.photo = request.FILES["photo"]
            compte.save()

            etudiant.nom = form.cleaned_data["nom"]
            etudiant.prenom = form.cleaned_data["prenom"]
            etudiant.sexe = form.cleaned_data["sexe"]
            etudiant.date_de_naissance = form.cleaned_data["date_de_naissance"]
            etudiant.pays = form.cleaned_data["pays"]
            etudiant.groupe_sanguin = form.cleaned_data["groupe_sanguin"]

            print(etudiant.nom)

            annee = datetime.strptime(etudiant.date_de_naissance, "%d/%m/%Y").year

            etudiant.matricule = (
                "ET"
                + "{:04d}".format(etudiant.compte.pk)
                + etudiant.sexe
                + str(annee)
                + get_country_code(etudiant.pays)
            )

            etudiant.save()

            return redirect("etudiants:etudiant", etudiant.pk)

    if details is not None:
        for detail in details:
            modules = Module.objects.filter(
                specialite=detail.specialite, grade=detail.grade
            )
            for module in modules:
                for matiere in Matiere.objects.filter(module=module):
                    if matiere is not None:
                        matieres.append(matiere)

    context = {
        "etudiant": etudiant,
        "details": details,
        "matieres": matieres,
        "form": form,
    }
    return render(request, "etudiants/etudiant_detail.html", context)


