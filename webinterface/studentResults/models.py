from turtle import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    studentNumber = models.CharField(max_length=3, primary_key=True, default='no value')
    assignmentOne = models.CharField(max_length=3, null=True, blank=True)
    assignmentTwo = models.CharField(max_length=3, null=True , blank=True)
    assignmentThree = models.CharField(max_length=3, null=True , blank=True)
    assignmentFour = models.CharField(max_length=3, null=True, blank=True)
    assignmentFive = models.CharField(max_length=3, null=True, blank=True)
    assignmentSix = models.CharField(max_length=3, null=True, blank=True)
    testOne = models.CharField(max_length=3, null=True, blank=True)
    testTwo = models.CharField(max_length=3, null=True, blank=True)
    finalMark = models.CharField(max_length=3, null=True, blank=True)
    assignmentAverage = models.CharField(max_length=3, null=True, blank=True)
    testAverage = models.CharField(max_length=3, null=True, blank=True)

