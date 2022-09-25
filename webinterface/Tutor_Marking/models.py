from django.db import models

# Create your models here.
class Tutor_Marking(models.Model): #name of the table  
    student= models.CharField(max_length = 3, primary_key=True, default='no value')
    A1_Marker = models.CharField(max_length=15, blank= True, null = True)
    A2_Marker = models.CharField(max_length=15, blank= True, null = True)
    A3_Marker = models.CharField(max_length=15, blank= True, null = True)
    A4_Marker = models.CharField(max_length=15, blank= True, null = True)
    A5_Marker = models.CharField(max_length=15, blank= True, null = True)
    A6_Marker = models.CharField(max_length=15, blank= True, null = True)
    