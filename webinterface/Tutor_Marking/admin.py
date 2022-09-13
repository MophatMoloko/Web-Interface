from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models 

# Register your models here.

class TutorMarkingAdmin(admin.ModelAdmin):
    pass

class TutorMarkingAdmin(ImportExportModelAdmin):
    pass

admin.site.register(models.Tutor_Marking, TutorMarkingAdmin)

