
from django.shortcuts import render
from http.client import HTTPResponse
from django.views.generic import ListView, DetailView
from webinterface.settings import BASE_DIR
from .models import Tutor_Marking
from xlsx2html import xlsx2html 



# Create your views here.

#Gives a list of all the tutors for each assignment marked
class ListTutorMarking(ListView):
    model = Tutor_Marking
    context_object_name ="students"
    template_name = 'Tutor_Marking/markers.html'

    def get_queryset(self):
        return Tutor_Marking.objects.all()

class TutorsDetail(DetailView):
    model = Tutor_Marking
    context_object_name ="student"
    template_name = 'Tutor_Marking/tutor_detail.html'



    
    
        

