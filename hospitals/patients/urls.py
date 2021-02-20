from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('queue/', views.patientqueue),
    path('administration/', views.administration),
]