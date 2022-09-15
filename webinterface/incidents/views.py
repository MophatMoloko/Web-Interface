from http.client import HTTPResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import IncidentsForm
from .models import Incidents
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#Creates a class to delete requests made by a student
#Takes in a generic view from Django framework
class IncidentsDeleteView(DeleteView):
    model = Incidents
    success_url = '/smart/incidents'
    template_name = 'incidents/incidents_delete.html'

#Creates a class to edit a request made by a student
#Takes in a generic view from Django framework
class IncidentsUpdateView(UpdateView):
    model = Incidents
    success_url = '/smart/incidents'
    form_class = IncidentsForm

#Creates a class to create a new request from the user
#Takes in a generic view from Django framework
#Requires a user to be logged in to view requests
class IncidentsCreateView(LoginRequiredMixin, CreateView):
    model = Incidents
    success_url = '/smart/incidents'
    form_class = IncidentsForm
    login_url ="/admin"
    #query_type = 

    #The function saves the items of the form first before sending to
    #backend database
    #The funtion takes in the logged in user and the form the user is completing
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


#Creates a class to view all requests a user has made
#Takes in a generic view from Django framework
#Requires a user to be logged in to view request
class IncidentsListView(LoginRequiredMixin, ListView):
    model = Incidents
    context_object_name = "incidents"
    template_name ='incidents/incidents_list.html'
    login_url = "/admin"

    #This funtion tests if user is Convener to show all requests
    #else, only show a request of the logged in user
    def get_queryset(self):
        if self.request.user.is_superuser:
             Users = Incidents.objects.all().order_by('created')
        else:
            Users = self.request.user.incidents.all().order_by('created')
        return Users

#Creates a class to view only selected request
#Takes in a generic view from Django framework
class IncidentsDetailView(DetailView):
    model = Incidents
    context_object_name= "incident"
    template_name = 'incidents/incident_detail.html'
