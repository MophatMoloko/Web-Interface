from django.db import models


class Incidents(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
