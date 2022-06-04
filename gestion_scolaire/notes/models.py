from django.db import models

from cours.models import Matiere
from etudiants.models import Etudiant
from enseignants.models import Enseignant


TYPE_EXAMENS = (
    ("Devoir", "Devoir"),
    ("Examen", "Examen"),
    ("Rattrappage", "Rattrappage"),
)


class Evaluation(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    type_evaluation = models.CharField(max_length=20, choices=TYPE_EXAMENS)


class Note(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="notes")
    moyenne = models.DecimalField(max_digits=4, decimal_places=2, default=0)
