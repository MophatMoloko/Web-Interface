from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Incidents
from django.db import models

#QUERY_TYPE = (
#        ("MC", "Medical Certificate"),
#        ("CG", "Compassionate Grounds"),
#        ("W", "Waive"),
#    )

#Creates a form with all the required fields for the user to complete
class IncidentsForm(forms.ModelForm):
    
    class Meta:
        model = Incidents
        fields = ('title', 'text', 'upload', 'query_type')
        labels = {
            'text': 'Write accompanying message for the request:',
            'query_type': 'Please select query category:',
        }
        #query_type = models.CharField(max_length=2, choices = QUERY_TYPE, default = "MC")
    #class Catagory:


    #def clean_title(self):
     #   title = self.cleaned_data['title']
      #  if 'Convener' not in title:
       #     raise ValueError("We only accept incidents for the Converner")
        #return title