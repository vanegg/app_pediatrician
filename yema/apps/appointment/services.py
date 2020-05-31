from django.core.mail import send_mass_mail
from django.core import mail
from yema.apps.users.models import User
from django.utils.translation import gettext_lazy as _


class MailAppointmentService():
    def send(self, appointments):
        mails = self.__build_mails(appointments)
        send_mass_mail(mails, fail_silently=False)


    def __build_mails(self, appointments):
        mails = []
        subject_base = _("Appointment Confirmation id: %(id)s")
        comments_base = _("Hi Dr %(name)s: \nYou have a new appointment of %(email)s, \nDate: %(date)s - %(time)s \nComments: %(comments)s \nPlease accept/reject it :)")

        for appointment in appointments:
            mail_tuple = (subject_base % { 'id': appointment.id }, 
                          comments_base % {'name': appointment.doctor_name, 
                                            'email': appointment.email, 
                                            'date' : appointment.date, 
                                            'time' : appointment.time, 
                                            'comments' : appointment.comments},
                    'hola@yema.com', 
                    [appointment.doctor_email])
            mails.append(mail_tuple)
        return (*mails, )
