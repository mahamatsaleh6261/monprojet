from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction

from staffs.views import is_not_anonymous, is_enseignant
from enseignants.models import Enseignant
from cours.models import Matiere, Attribution
from parcours.models import Specialite
from etudiants.models import Etudiant, Inscription

from .models import Evaluation, Note
from .forms import EvaluationForm, NoteForm


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def evaluation_create_view(request, pk):
    attribution = get_object_or_404(Attribution, pk=pk)
    form = EvaluationForm()

    if request.method == "POST":
        form = EvaluationForm(request.POST)
        if form.is_valid():
            enseignant = attribution.enseignant
            matiere = attribution.matiere
            annee = attribution.annee
            grade = attribution.matiere.module.grade
            date = form.cleaned_data["date"]
            type_evaluation = form.cleaned_data["type_evaluation"]

            evaluation = Evaluation.objects.create(
                enseignant=enseignant,
                matiere=matiere,
                type_evaluation=type_evaluation,
                date=date,
                annee=annee,
            )

            specialite = matiere.module.specialite

            inscriptions = Inscription.objects.filter(
                specialite=specialite,
                annee=annee,
                grade=grade,
            )

            for inscription in inscriptions:
                Note.objects.create(
                    evaluation=evaluation,
                    etudiant=inscription.etudiant,
                )

            return redirect("notes:ajouter", attribution.pk)

    return render(request, "notes/evaluation.html", {"form": form})


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def evaluation_list_view(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    evaluations = Evaluation.objects.filter(enseignant=enseignant)
    context = {"evaluations": evaluations}

    return render(request, "notes/evaluation_list.html", context)


@user_passes_test(is_not_anonymous, login_url="/")
@user_passes_test(is_enseignant, login_url="/")
@login_required(login_url="/")
def evaluation_note_create_view(request, pk):
    evaluation = get_object_or_404(Evaluation, pk=pk)
    notes = Note.objects.filter(evaluation=evaluation)

    if request.method == "POST":
        for note in notes:
            note.moyenne = request.POST.get(note.etudiant.matricule)
            note.save()

        return redirect("notes:notes", evaluation.pk)

    context = {"evaluation": evaluation, "notes": notes}
    return render(request, "notes/evaluation_list.html", context)
