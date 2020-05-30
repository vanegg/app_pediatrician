from django import forms
from django.db import models
from django.contrib import admin
from django.utils import timezone
from .models import Appointment
from .validators import AppointmentValidator


import datetime 

HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 20)]


class AppointmentForm(forms.ModelForm):    
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {'time': forms.Select(choices=HOUR_CHOICES)}
