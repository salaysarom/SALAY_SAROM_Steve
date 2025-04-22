from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nom} ({self.specialite})"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date} - {self.patient} avec {self.medecin}"
