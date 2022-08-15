from django.shortcuts import render
from .models import Incidents
from django.views.generic import CreateView, DetailView, ListView


class IncidentsCreateView(CreateView):
    model = Incidents
    fields = ('title', 'text', 'upload')
    success_url = '/smart/incidents'

class IncidentsListView(ListView):
    model = Incidents
    context_object_name = "incidents"
    template_name ='incidents/incidents_list.html'

class IncidentsDetailView(DetailView):
    model = Incidents
    context_object_name= "incident"
    template_name = 'incidents/incident_detail.html'
