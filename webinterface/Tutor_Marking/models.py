from django.db import models


# Create your models here.
class Tutor_Marking(models.Model): #name of the table 
    
    A1_Marker = models.CharField(max_length=20, blank=False)
    A2_Marker = models.CharField(max_length=20, blank=False)
    A3_Marker = models.CharField(max_length=20, blank=False)
    A4_Marker = models.CharField(max_length=20, blank=False)
    A5_Marker = models.CharField(max_length=20, blank=False)
    A6_Marker = models.CharField(max_length=20, blank=False)
    
    def __str__(self) -> str:
        return 
    