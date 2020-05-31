from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Doctor(models.Model):
    user = models.OneToOneField(User, 
                        on_delete=models.CASCADE, 
                        primary_key=True,
                        verbose_name=_('user'))

    def __str__(self):
        return self.user.get_full_name()

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email

    class Meta:
        verbose_name = _('doctor')
        verbose_name_plural = _('doctors')


class Patient(models.Model):
    user = models.OneToOneField(User, 
                            on_delete=models.CASCADE, 
                            primary_key=True,
                            verbose_name=_('user'))

    def __str__(self):
        return self.user.get_full_name()

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email
    
    class Meta:
        verbose_name = _('patient')
        verbose_name_plural = _('patients')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_doctor:
        Doctor.objects.get_or_create(user=instance)
    elif instance.is_patient:
        Patient.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_doctor:
        instance.doctor.save()
    elif instance.is_patient:
        instance.patient.save()
