from django.db import models

from parcours.models import Specialite
from enseignants.models import Enseignant


GRADES = (
    ("L1", "Licence 1"),
    ("L2", "Licence 2"),
    ("L3", "Licence 3"),
    ("M1", "Master 1"),
    ("M2", "Master 2"),
)


SEMESTRES = (
    ("S1", "Semestre 1"),
    ("S2", "Semestre 2"),
)


class Module(models.Model):
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, related_name="modules")
    grade = models.CharField(max_length=20, choices=GRADES)
    semestre = models.CharField(max_length=20, choices=SEMESTRES)
    code = models.CharField(max_length=20)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return (
            self.nom
            + " --> "
            + self.semestre
            + " - "
            + self.grade
            + " - "
            + self.specialite.sigle
        )


class Matiere(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="matieres")
    code = models.CharField(max_length=20)
    nom = models.CharField(max_length=255)
    credit = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Attribution(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee = models.CharField(max_length=20)
