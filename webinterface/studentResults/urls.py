from django.urls import path
from . import views

#These are all the accepted URL's for the Incidents application
urlpatterns = [
     path('students', views.simple_upload, name="upload"),
     path('results', views.StudentResults.as_view(), name="results"),
]