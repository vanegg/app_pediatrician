from django.core.mail import send_mass_mail
from django.core import mail
from yema.apps.users.models import User


class MailAppointmentService():
    def send(self, appointments):
        mails = self.__build_mails(appointments)
        send_mass_mail(mails, fail_silently=False)


    def __build_mails(self, appointments):
        mails = []
        subject_base = "Appointment Confirmation id: %s"
        comments_base = "Hi Dr %s: \nYou have a new appointment of %s, \nDate: %s \nComments: %s \nPlease accept/reject it :)"

        for appointment in appointments:
            mail_tuple = (subject_base % (appointment.id), 
                    comments_base % (appointment.doctor_name, appointment.email, appointment.appointment_date, appointment.comments),
                    'hola@yema.com', 
                    [appointment.doctor_email])
            mails.append(mail_tuple)
        return (*mails, )
