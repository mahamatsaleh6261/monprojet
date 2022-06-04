from django import forms
from .models import Domain, Mention


class DomainCreationForm(forms.Form):
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Domaine",
            }
        ),
        max_length=255,
    )


class MentionCreationForm(forms.Form):
    domain = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Domaine",
            }
        ),
        queryset=Domain.objects.all(),
        empty_label="------------------------------",
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Mention",
            }
        ),
        max_length=255,
    )


class SpecialiteCreationForm(forms.Form):
    mention = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-select shadow-none",
                "id": "floatingInput",
                "placeholder": "Mention",
            }
        ),
        queryset=Mention.objects.all(),
        empty_label="------------------------------",
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Spécialité",
            }
        ),
        max_length=255,
    )
    sigle = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Sigle",
            }
        ),
        max_length=20,
    )
