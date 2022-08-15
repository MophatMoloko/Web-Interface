from django.contrib import admin
from . import models

class IncidentsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Incidents, IncidentsAdmin)