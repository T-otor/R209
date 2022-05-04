from django.db import models

# Create your models here.
class RAM(models.Model): 
    Marque = models.CharField(max_length=100) 
    Modèle = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 4)
    Capacité = models.CharField(max_length=20)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"Barrette {self.Marque}, modèle {self.Modèle}, de la {self.Type} avec une capacité de {self.Capacité}"
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, 'Type': self.Type, 'Capacité': self.Capacité, 'SN': self.SN}

class CPU(models.Model): 
    Marque = models.CharField(max_length=100) 
    Modèle = models.CharField(max_length = 100)
    Fréquence = models.CharField(max_length = 4)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"CPU {self.Marque}, modèle {self.Modèle}, avec une fréquence de {self.Fréquence} "
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, "Fréquence": self.Fréquence, "SN": self.SN}
    

class HDD(models.Model): 
    Marque = models.CharField(max_length=100) 
    Modèle = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 4)
    Espace = models.CharField(max_length=40)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"CPU {self.Marque}, modèle {self.Modèle}, Type {self.Type}, avec un espace de stockage de {self.Espace} "
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, "Type": self.Type, "Espace": self.Espace, "SN": self.SN}


