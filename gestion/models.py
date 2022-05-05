from django.db import models

class Marque(models.Model):
    Marque = models.CharField(max_length=100)
    def __str__(self):
        chaine = f"{self.Marque}"
        return chaine

class Type(models.Model):
    Type = models.CharField(max_length=100)

# Create your models here.
class RAM(models.Model): 
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    Modèle = models.CharField(max_length = 100)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    Capacité = models.CharField(max_length=20)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"Barrette {self.Marque}, modèle {self.Modèle}, de la {self.Type} avec une capacité de {self.Capacité}"
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, 'Type': self.Type, 'Capacité': self.Capacité, 'SN': self.SN}

class CPU(models.Model): 
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    Modèle = models.CharField(max_length = 100)
    Fréquence = models.CharField(max_length = 10)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"CPU {self.Marque}, modèle {self.Modèle}, avec une fréquence de {self.Fréquence} "
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, "Fréquence": self.Fréquence, "SN": self.SN}
    

class HDD(models.Model): 
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    Modèle = models.CharField(max_length = 100)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    Espace = models.CharField(max_length=40)
    SN = models.CharField(max_length=20)
    
    def __str__(self):
        chaine = f"CPU {self.Marque}, modèle {self.Modèle}, Type {self.Type}, avec un espace de stockage de {self.Espace} "
        return chaine
    def dico(self):
        return {'Marque': self.Marque, "Modèle": self.Modèle, "Type": self.Type, "Espace": self.Espace, "SN": self.SN}


