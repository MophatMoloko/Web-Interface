from django.shortcuts import render
from http.client import HTTPResponse
from django.views.generic import TemplateView

from webinterface.settings import BASE_DIR
from .models import Tutor_Marking
import os


# Create your views here.

#Gives a list of all the tutors for each assignment marked
#
class ListTutorMarking(TemplateView):
    model = Tutor_Marking
    template_name = os.path.join(BASE_DIR,"Tutor_Marking", "templates", "markers.html")
    success_url= 'smart/Tutor_Marking'
    
    def show(request): 
        queryset = Tutor_Marking.objects.all()
        context = {'Marks_Table' : queryset}
        return render(request,"Tutor_Markers", context)
   

