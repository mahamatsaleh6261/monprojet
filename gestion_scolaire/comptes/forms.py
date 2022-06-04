from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Compte


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Adresse email",
                "autocomplete": "off",
            }
        ),
        max_length=255,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Mot de passe",
                "autocomplete": "new-password",
            }
        ),
        max_length=255,
    )


class UserSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        help_text="<ul class='errorlist text-muted'><li>Your password can 't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can 't be a commonly used password.</li> <li>Your password can 't be entirely numeric.<li></ul>",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Nouveau mot de passe",
                "type": "password",
            }
        ),
    )

    new_password2 = forms.CharField(
        help_text=False,
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control shadow-none",
                "id": "floatingInput",
                "placeholder": "Confirmer votre mot de passe",
                "type": "password",
            }
        ),
    )
