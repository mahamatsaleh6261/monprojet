from django.db import models


class Domain(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Mention(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Specialite(models.Model):
    mention = models.ForeignKey(Mention, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, unique=True)
    sigle = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
