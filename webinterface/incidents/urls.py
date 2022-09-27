from django.urls import path
from . import views

#These are all the accepted URL's for the Incidents application
urlpatterns = [
    path('incidents', views.IncidentsListView.as_view(), name="incidents.list"),
    path('email', views.post, name="send"),
    path('summary', views.IncidentsSummary.as_view(), name="summary.list"),
    path('incidents/<int:pk>', views.IncidentsDetailView.as_view(), name="incidents.detail"),
    path('incidents/<int:pk>/edit', views.IncidentsUpdateView.as_view(), name="incidents.update"),
    path('incidents/<int:pk>/delete', views.IncidentsDeleteView.as_view(), name="incidents.delete"),
    path('incidents/new', views.IncidentsCreateView.as_view(), name="incidents.new"),
]