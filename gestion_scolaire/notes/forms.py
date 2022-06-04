from django import forms
from datetime import date

from enseignants.models import Enseignant
from cours.models import Matiere
from etudiants.models import Etudiant

from .models import Evaluation, Note, TYPE_EXAMENS


class EvaluationForm(forms.Form):
    date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "datepicker_input form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "JJ/MM/AAAA",
            }
        ),
        max_length=255,
    )
    type_evaluation = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Type",
            }
        ),
        choices=TYPE_EXAMENS,
    )


class NoteForm(forms.Form):
    evaluation = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Evaluation",
            }
        ),
        queryset=Evaluation.objects.all(),
        empty_label="",
    )
    etudiant = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Etudiant",
            }
        ),
        queryset=Etudiant.objects.all(),
        empty_label="",
    )
    moyenne = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Moyenne",
            }
        ),
        max_length=255,
    )
