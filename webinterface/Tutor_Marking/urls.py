from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('Tutor_Marking',views.ListTutorMarking.as_view(), name="Tutor_List"),
    path('tutor_upload', views.simple_uploads, name = "uploads")
]