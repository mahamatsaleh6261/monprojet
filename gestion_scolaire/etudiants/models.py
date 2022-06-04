from django.db import models

from comptes.models import Compte, Information
from parcours.models import Specialite
from cours.models import GRADES


GROUPE_SANGUIN = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-"),
)


class Etudiant(Information):
    compte = models.OneToOneField(
        Compte, primary_key=True, on_delete=models.CASCADE, related_name="etudiant"
    )
    groupe_sanguin = models.CharField(choices=GROUPE_SANGUIN, max_length=20)


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="inscriptions")
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    grade = models.CharField(max_length=20, choices=GRADES)
    annee = models.CharField(max_length=20)
