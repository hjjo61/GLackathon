from django.db import models

# Create your models here.
class Patients(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastphone = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    checkin_time = models.DateTimeField(auto_now_add=True)