from django import forms

from pays import Countries
from datetime import date

from parcours.models import Specialite
from cours.models import GRADES
from comptes.models import SEXES

from .models import Etudiant, GROUPE_SANGUIN


PAYS = list()
for country in Countries():
    PAYS.append((country.name, country.name))

year = date.today().year - 3

ANNEES = (
    ((f'{year}{" - "}{year + 1}'), (f'{year}{" - "}{year + 1}')),
    ((f'{year + 1}{" - "}{year + 2}'), (f'{year + 1}{" - "}{year + 2}')),
    ((f'{year + 2}{" - "}{year + 3}'), (f'{year + 2}{" - "}{year + 3}')),
    ((f'{year + 3}{" - "}{year + 4}'), (f'{year + 3}{" - "}{year + 4}')),
    ((f'{year + 4}{" - "}{year + 5}'), (f'{year + 4}{" - "}{year + 5}')),
    ((f'{year + 5}{" - "}{year + 6}'), (f'{year + 5}{" - "}{year + 6}')),
)


class EtudiantCreationForm(forms.Form):
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
    prenom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Prénom",
            }
        ),
        max_length=255,
    )
    date_de_naissance = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "datepicker_input form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "JJ/MM/AAAA",
            }
        ),
        max_length=255,
    )
    sexe = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=SEXES,
    )
    pays = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=PAYS,
    )
    groupe_sanguin = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=GROUPE_SANGUIN,
    )
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control form-control-lg shadow-none",
                "id": "formFileLg",
                "placeholder": "Email",
            }
        ),
        max_length=255,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Email",
            }
        ),
        max_length=255,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Téléphone",
            }
        ),
        max_length=255,
    )


class EtudiantUpdateForm(forms.Form):
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
    prenom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Prénom",
            }
        ),
        max_length=255,
    )
    date_de_naissance = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "datepicker_input form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "JJ/MM/AAAA",
            }
        ),
        max_length=255,
    )
    sexe = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=SEXES,
    )
    pays = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=PAYS,
    )
    groupe_sanguin = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Sexe",
            }
        ),
        choices=GROUPE_SANGUIN,
    )
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control form-control-lg shadow-none",
                "id": "formFileLg",
                "placeholder": "Email",
            }
        ),
        max_length=255,
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Téléphone",
            }
        ),
        max_length=255,
    )


class InscriptionForm(forms.Form):
    specialite = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Spécialité",
            }
        ),
        queryset=Specialite.objects.all(),
        empty_label="----------------------------",
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
