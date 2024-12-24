from django.db import models

class Etudiant(models.Model):
    CLASSE_CHOICES = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3'),
        ('M1', 'Master 1'),
        ('M2', 'Master 2'),
    ]

    nom = models.CharField(max_length=250)
    email = models.CharField(max_length=255, unique=True)
    telephone = models.CharField(max_length=15)
    classe_choix = models.CharField(max_length=10, choices=CLASSE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom} ({self.email}) {self.classe_choix}"
