from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('Tutor_Marking',views.ListTutorMarking.as_view(), name="Tutor_Markers"),
]