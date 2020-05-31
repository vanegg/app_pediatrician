from django.db import models
from django.utils import timezone
from yema.apps.users.models import User, Doctor, Patient
from .validators import AppointmentValidator
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    APPOINTMENTS_STATUSES = (
        ('validating', _('validating')),
        ('approved', _('approved')),
        ('rejected', _('rejected')),
        ('completed', _('completed')),
    )
    doctor = models.ForeignKey(Doctor,
                            related_name='doctor_user',
                            on_delete=models.DO_NOTHING,
                            verbose_name=_('doctor'))
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True, verbose_name=_('comments'))
    date = models.DateField(default=timezone.now, 
                        validators=[AppointmentValidator().validate_future_date], 
                        verbose_name=_('appointment_date'))
    time = models.TimeField(default=timezone.now, verbose_name=_('appointment_hour'))
    status = models.CharField(max_length=15,
                              choices=APPOINTMENTS_STATUSES,
                              default='validating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    class Meta:
        unique_together = ("doctor", "date", "time")
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    @property
    def doctor_name(self):
        return self.doctor

    @property
    def doctor_email(self):
        return self.doctor.user.email
