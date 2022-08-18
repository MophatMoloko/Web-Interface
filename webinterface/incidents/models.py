from django.db import models
from django.contrib.auth.models import User

#This is a class model of how our database is configured
# that saves all the requred fields in the database
class Incidents(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidents")
