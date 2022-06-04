from django import forms

from pays import Countries

from cours.models import Matiere
from comptes.models import SEXES

from .models import Enseignant

PAYS = list()

for country in Countries():
    PAYS.append((country.name, country.name))


class EnseignantCreationForm(forms.Form):
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


class EnseignantUpdateForm(forms.Form):
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
