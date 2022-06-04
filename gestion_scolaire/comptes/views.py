from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, user_passes_test

from staffs.models import Staff
from enseignants.models import Enseignant
from etudiants.models import Etudiant
from notes.models import Note
from staffs.views import is_staff, is_not_anonymous, is_etudiant


from .tokens import account_activation_token
from .forms import LoginForm, UserSetPasswordForm
from .models import Compte


def login_view(request):

    if request.user.is_authenticated:
        if request.user.type_de_compte == "AD":
            return redirect("staffs:staffs")
        elif request.user.type_de_compte == "ST":
            return redirect("etudiants:etudiants")
        elif request.user.type_de_compte == "EN":
            return redirect("enseignants:matieres")
        else:
            return redirect("etudiants:matieres")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(username=email, password=password)

            if user is not None and user.is_active:
                login(request, user)

                if request.user.type_de_compte == "AD":
                    return redirect("staffs:staffs")
                elif request.user.type_de_compte == "ST":
                    return redirect("etudiants:etudiants")
                elif request.user.type_de_compte == "EN":
                    return redirect("enseignants:matieres")
                else:
                    return redirect("etudiants:matieres")

    form = LoginForm()
    return render(request, "comptes/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("comptes:login")


def set_password_view(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Compte.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Compte.DoesNotExist) as e:
        user = None

    if request.method == "POST":

        if user is not None and account_activation_token.check_token(user, token):

            form = UserSetPasswordForm(user=user, data=request.POST)

            if form.is_valid():
                form.save()
                user.save()

                return redirect("comptes:login")
        else:
            return HttpResponse("Lien d'activation invalide!")

    context = {"form": UserSetPasswordForm(user), "uid": uidb64, "token": token}
    return render(request, "comptes/password_reset.html", context)


def activate_account_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Compte.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Compte.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect("comptes:set_password", uidb64, token)
    else:
        return HttpResponse("Lien d'activation invalide!")


@receiver(post_save, sender=Compte)
def send_mail(sender, instance, created, **kwargs):
    if created:
        current_site = Site.objects.get_current()
        mail_subject = "Activation du compte"
        message = render_to_string(
            "comptes/activation_mail.html",
            {
                "user": instance,
                "protocol": "http",
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(instance.pk)),
                "token": account_activation_token.make_token(instance),
            },
        )

        to_email = instance.email
        activation_email = EmailMessage(mail_subject, message, to=[to_email])
        activation_email.send()


@receiver(post_save, sender=Note)
def evaluation_mail(sender, instance, created, **kwargs):
    if created:
        current_site = Site.objects.get_current()
        mail_subject = "Annonce d'évaluation"
        message = render_to_string(
            "comptes/evaluation_mail.html",
            {
                "note": instance,
                "protocol": "http",
                "domain": current_site.domain,
            },
        )

        to_email = instance.etudiant.compte.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()



@user_passes_test(is_not_anonymous, login_url="/")
@login_required(login_url="/")
def profil_detail_view(request):
    
    return render(request, "comptes/profil_detail.html", {})