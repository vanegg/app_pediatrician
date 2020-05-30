from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Appointment
from .forms import AppointmentForm
from .services import MailAppointmentService
from yema.apps.users.models import User


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['email', 'doctor_name', 'date', 'time','status','comments']
    ordering = ['date', 'time']
    actions = ['accept_appointment', 
              'cancel_appointment', 
              'reject_appointment', 
              'complete_appointment',
              'send_email_to_doctor']
    
    exclude = ['status', 'created_at', 'updated_at']
    form = AppointmentForm

    def accept_appointment(self, request, queryset):
        self.__update_status_appointment(request, queryset, 'approved')
    accept_appointment.short_description = "Accept appointment"

    def reject_appointment(self, request, queryset):
        self.__update_status_appointment(request, queryset, 'rejected')
    reject_appointment.short_description = "Reject appointment"

    def complete_appointment(self, request, queryset):
        self.__update_status_appointment(request, queryset, 'completed')
    complete_appointment.short_description = "Complete appointment"


    def __update_status_appointment(self, request, queryset, status):
        updated = queryset.update(status=status)
        self.message_user(request, ngettext(
            '%d story was successfully updated.',
            '%d stories were successfully updated.',
            updated,
        ) % updated, messages.SUCCESS)

    def send_email_to_doctor(self, request, queryset):
        MailAppointmentService().send(queryset)
    send_email_to_doctor.short_description = 'Send email to doctor'


admin.site.register(Appointment, AppointmentAdmin)
