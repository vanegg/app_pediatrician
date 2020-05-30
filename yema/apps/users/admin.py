from django.contrib import admin
from .models import User, Doctor, Patient


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'full_name']
    ordering = ['user']
  

class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'full_name']
    ordering = ['user']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name']
    fields = ['username', 'first_name', 'last_name', 'email', 'password']


admin.site.register(User, UserAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
