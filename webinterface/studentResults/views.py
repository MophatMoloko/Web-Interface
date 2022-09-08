import imp
from django.shortcuts import render
from .models import Student
from .resources import StudentResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def simple_upload(request):
    success_url ='/home'
    template_name = 'studentResults/templates/upload.html'
    if request.method == "POST":
        student_resource = StudentResource()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, "Wrong format")
            return render(request,'upload.html')

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
    return render(request, 'upload.html')
            