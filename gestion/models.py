from django.db import models

# Create your models here.
class RAM(models.Model): 
    Marque = models.CharField(max_length=100) 
    Modèle = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 4)
    Capacité = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"Barrette {self.Marque}, modèle {self.Modèle}, de la {self.Type} avec une capacité de {self.Capacité}"
        return chaine