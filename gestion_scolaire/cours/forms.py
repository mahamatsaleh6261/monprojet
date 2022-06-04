from django import forms
from datetime import date

from parcours.models import Specialite
from enseignants.models import Enseignant

from .models import Module, GRADES, SEMESTRES


year = date.today().year - 3

ANNEES = (
    ((f'{year}{" - "}{year + 1}'), (f'{year}{" - "}{year + 1}')),
    ((f'{year + 1}{" - "}{year + 2}'), (f'{year + 1}{" - "}{year + 2}')),
    ((f'{year + 2}{" - "}{year + 3}'), (f'{year + 2}{" - "}{year + 3}')),
    ((f'{year + 3}{" - "}{year + 4}'), (f'{year + 3}{" - "}{year + 4}')),
    ((f'{year + 4}{" - "}{year + 5}'), (f'{year + 4}{" - "}{year + 5}')),
    ((f'{year + 5}{" - "}{year + 6}'), (f'{year + 5}{" - "}{year + 6}')),
)


class ModuleCreationForm(forms.Form):
    specialite = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Spécialité",
            }
        ),
        queryset=Specialite.objects.all(),
        empty_label="------------------------------",
    )
    grade = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Grade",
            }
        ),
        choices=GRADES,
    )
    semestre = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Semestre",
            }
        ),
        choices=SEMESTRES,
    )
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Code",
            }
        ),
        max_length=255,
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Nom",
            }
        ),
        max_length=255,
    )


class MatiereCreationForm(forms.Form):
    module = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Module",
            }
        ),
        queryset=Module.objects.all(),
        empty_label="------------------------------",
    )
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Code",
            }
        ),
        max_length=255,
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Nom",
            }
        ),
        max_length=255,
    )
    credit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Crédit",
            }
        ),
        max_length=2,
    )


class ProgrammeCreationForm(forms.Form):
    enseignant = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Enseignant",
            }
        ),
        queryset=Enseignant.objects.all(),
        empty_label="------------------------------",
    )
    annee = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Année Académique",
            }
        ),
        choices=ANNEES,
    )
