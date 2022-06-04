from django.db import models

from comptes.models import Compte, Information


class Staff(Information):
    compte = models.OneToOneField(
        Compte, primary_key=True, on_delete=models.CASCADE, related_name="staff"
    )

    def __str__(self):
        return self.nom + " " + self.prenom
