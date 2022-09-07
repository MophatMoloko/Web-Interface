from django.shortcuts import render
from http.client import HTTPResponse
from django.views.generic import TemplateView
from .models import Tutor_Marking
import os


# Create your views here.

#Gives a list of all the tutors for each assignment marked
#
class ListTutorMarking(TemplateView):
    model = Tutor_Marking
    template_name = os.path.join( "Tutor_Marking", "templates", "markers.html")
    success_url= 'smart/tutor_marking'
    
    
    
