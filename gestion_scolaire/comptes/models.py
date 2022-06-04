from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from pays import Countries


SEXES = (
    ("M", "Masculin"),
    ("F", "Féminin"),
)


TYPE_DE_COMPTES = (
    ("AD", "Administrateur"),
    ("ST", "Staff"),
    ("EN", "Enseignant"),
    ("ET", "Etudiant"),
)


def get_country_code(country_name):
    pays = {}

    for country in Countries():
        pays[country.name] = country.cca2

    return pays[country_name]


class GestionDeCompte(BaseUserManager):
    def create_user(self, email, telephone, password, type_de_compte, **extra_fields):

        if not email:
            raise ValueError("Veuillez saisir l'email")

        email = self.normalize_email(email)
        compte = self.model(
            email=email, telephone=telephone, type_de_compte=type_de_compte
        )
        compte.set_password(password)
        compte.save()

        return compte

    def create_superuser(
        self, email, telephone, password, type_de_compte, **extra_fields
    ):
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            email, telephone, password, type_de_compte, **extra_fields
        )


class Compte(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    telephone = models.CharField(max_length=24)
    type_de_compte = models.CharField(max_length=30, choices=TYPE_DE_COMPTES)
    photo = models.ImageField(upload_to="comptes/images", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["telephone", "type_de_compte"]

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = GestionDeCompte()


class Information(models.Model):
    matricule = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_de_naissance = models.CharField(max_length=20)
    pays = models.CharField(max_length=255)
    sexe = models.CharField(max_length=30, choices=SEXES)

    class Meta:
        abstract = True
