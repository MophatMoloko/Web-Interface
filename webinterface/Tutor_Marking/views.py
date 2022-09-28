
from django.shortcuts import render
from http.client import HTTPResponse
from django.views.generic import ListView, DetailView
from webinterface.settings import BASE_DIR
from .models import Tutor_Marking
from tablib import Dataset
from django.contrib import messages

#Gives a list of all the tutors for each assignment marked
def simple_uploads(request):
    if request.method == "POST":
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, "Wrong format")
            return render(request,'Tutor_Marking/markers.html')

        imported_data = dataset.load(new_student.read(),format='xlsx')
        for data in imported_data:
            value = Tutor_Marking(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6],
                            )
            value.save()
    return render(request, 'Tutor_Marking/markers.html')

class ListTutorMarking(ListView):
    model = Tutor_Marking
    context_object_name ="tutors"
    template_name = 'Tutor_Marking/tutor_marking_list'

    def get_queryset(self):
        return Tutor_Marking.objects.all()

class TutorsDetail(DetailView):
    model = Tutor_Marking
    context_object_name ="tutor"
    template_name = 'Tutor_Marking/tutor_detail.html'


    
    
        

