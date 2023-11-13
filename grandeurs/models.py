from django.db import models

class Grandeur(models.Model):
    nom= models.CharField(max_length=60)
    unite= models.CharField(max_length=30)
    valeurMin= models.FloatField()
    valeurMax= models.FloatField()

    def __str__(self) -> str:
        return f'Grandeur:  {self.nom} Unité:  {self.unite} Valeur entre {self.valeurMinx} et {self.valeurMax}'
    

class Mesure(models.Model):
    valeur= models.FloatField()
    datePrise= models.DateTimeField()
    grandeur = models.ForeignKey('Grandeur', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'Mesure:  {self.valeur} at {self.datePrise}'