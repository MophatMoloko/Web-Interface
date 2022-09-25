from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tutor_Marking

# Register your models here.
@admin.register(Tutor_Marking)
class TutorMarkingAdmin(ImportExportModelAdmin):
    list_display = ('student',
    'A1_Marker',
    'A2_Marker', 
    'A3_Marker',
    'A4_Marker',
    'A5_Marker',
    'A6_Marker')

