from http.client import HTTPResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import IncidentsForm
from .models import Incidents
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class IncidentsDeleteView(DeleteView):
    model = Incidents
    success_url = '/smart/incidents'
    template_name = 'incidents/incidents_delete.html'

class IncidentsUpdateView(UpdateView):
    model = Incidents
    success_url = '/smart/incidents'
    form_class = IncidentsForm

class IncidentsCreateView(LoginRequiredMixin, CreateView):
    model = Incidents
    success_url = '/smart/incidents'
    form_class = IncidentsForm
    login_url ="/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class IncidentsListView(LoginRequiredMixin, ListView):
    model = Incidents
    context_object_name = "incidents"
    template_name ='incidents/incidents_list.html'
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.incidents.all()

class IncidentsDetailView(DetailView):
    model = Incidents
    context_object_name= "incident"
    template_name = 'incidents/incident_detail.html'
