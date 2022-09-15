import imp
from django.shortcuts import render
from .models import Student
from .resources import StudentResource
from django.contrib import messages
from tablib import Dataset
from django.views.generic import ListView, DetailView


# Create your views here.
def simple_upload(request):

    if request.method == "POST":
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, "Wrong format")
            return render(request,'studentResults/upload.html')

        imported_data = dataset.load(new_student.read(),format='xlsx')
        for data in imported_data:
            value = Student(data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6],
                            data[7],
                            data[8],
                            data[9],
                            data[10],
                            data[11],
                            )
            value.save()

        if new_student.name.endswith('xlsx'):
            return render(request,'studentResults/success.html')

    return render(request, 'studentResults/upload.html')

class StudentResults(ListView):
    model = Student
    context_object_name ="students"
    template_name ='studentResults/results.html'

    def get_queryset(self):
        order_list = ['assignmentAverage','testAverage']
        return Student.objects.all().order_by(*order_list)

class StudentsDetailView(DetailView):
    model = Student
    context_object_name= "student"
    template_name = 'studentResults/detail_view.html'

