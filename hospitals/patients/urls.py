from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('queue/', views.patientqueue, name='queue'),
    path('administration/', views.administration, name='administration'),
]