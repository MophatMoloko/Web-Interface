from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Student

@admin.register(Student)
class StudentsAdmin(ImportExportActionModelAdmin):
    list_display = ("studentNumber",
                    "assignmentOne",
                    "assignmentTwo",
                    "assignmentThree",
                    "assignmentFour",
                    "assignmentFive",
                    "assignmentSix",
                    "testOne",
                    "testTwo",
                    "finalMark",
                    "assignmentAverage",
                    "testAverage")

