from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Incidents

#Creates a form with all the required fields for the user to complete
class IncidentsForm(forms.ModelForm):
    class Meta:
        model = Incidents
        fields = ('title', 'text', 'upload')
        labels = {
            'text': 'Write accompanying message for the request:'
        }

    #def clean_title(self):
     #   title = self.cleaned_data['title']
      #  if 'Convener' not in title:
       #     raise ValueError("We only accept incidents for the Converner")
        #return title