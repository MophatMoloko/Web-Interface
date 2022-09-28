from django.urls import path
from . import views

#All the accepted URL's in the Home application
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home' ),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout')
]