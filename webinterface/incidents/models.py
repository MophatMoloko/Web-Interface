from django.db import models
from django.contrib.auth.models import User

QUERY_TYPE = (
        ("Medical Certificate", "Medical Certificate"),
        ("Compassionate Grounds", "Compassionate Grounds"),
        ("Waive", "Waive"),
    )

#This is a class model of how our database is configured
# that saves all the requred fields in the database
class Incidents(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidents")
    query_type = models.CharField(max_length=30, choices = QUERY_TYPE, default = 'MC')

def __str__(self):
        return  self.title+'   '+ self.title + '   ' + self.text +'   ' + self.created + '   ' +self.query_type +'\n'
