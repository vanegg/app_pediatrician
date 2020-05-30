from django.db import models
from django.utils import timezone
from django.utils.translation import ngettext
from yema.apps.users.models import User, Doctor, Patient
from .managers import AppointmentManager
from .validators import AppointmentValidator

import datetime

class Appointment(models.Model):
    APPOINTMENTS_STATUSES = (
        ('validating', 'Validating'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    doctor = models.ForeignKey(Doctor,
                               related_name='doctor_user',
                               on_delete=models.DO_NOTHING)
    # patient = models.ForeignKey(Patient,
    #                             related_name='patient',
    #                             on_delete=models.DO_NOTHING)
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now, validators=[AppointmentValidator().validate_future_date])
    time = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=15,
                              choices=APPOINTMENTS_STATUSES,
                              default='validating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppointmentManager()

    def __str__(self):
        return self.email

    class Meta:
       unique_together = ("doctor", "date", "time")


    @property
    def doctor_name(self):
        return self.doctor


    @property
    def doctor_email(self):
        return self.doctor.user.email
