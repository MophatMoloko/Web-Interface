from http.client import HTTPResponse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import IncidentsForm, EmailForm
from .models import Incidents
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings

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

class IncidentsSummary(LoginRequiredMixin, ListView):
    model = Incidents
    context_object_name = "incidents"
    template_name ='incidents/summary.html'
    login_url = "/admin"

    #This funtion tests if user is Convener to show all requests
    #else, only show a request of the logged in user
    def get_queryset(self):
        return Incidents.objects.all()


   
def post(self, request):
        form_class = EmailForm
        form = self.form_class(request.POST)

        if form.is_valid():
           messageSent = False

    # check if form has been submitted
        if request.method == 'POST':
            form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = "testing via view "

            # send the email to the recipent
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

        else:
             form = EmailForm()

        return render(request, self.template_name, {'form': form})