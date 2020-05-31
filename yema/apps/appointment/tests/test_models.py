from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Appointment
from django.utils import timezone
from yema.apps.users.models import User, Doctor

import datetime

class AppointmentTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(first_name='John', last_name='Doe', email='johndoe@mail.com', username='jonhdoe', password='pass')
        doctor = Doctor.objects.create(user=user)
        date = datetime.date.today() + datetime.timedelta(days=5)
        cls.doctor_id = doctor.pk
        cls.obj_id = Appointment.objects.create(doctor=doctor, email='test@mail.com', date=date).pk


    def test_doctor_label(self):
        appointment = Appointment.objects.get(id=self.obj_id)
        field_label = appointment._meta.get_field('doctor').verbose_name
        self.assertEquals(field_label, 'Pediatra')
    
    
    def test_status_max_length(self):
        appointment = Appointment.objects.get(id=self.obj_id)
        max_length = appointment._meta.get_field('status').max_length
        self.assertEquals(max_length, 15)


    def test_appointment_with_date_in_past(self):
        doctor = Doctor.objects.get(pk=self.doctor_id)
        date   = datetime.date.today() - datetime.timedelta(days=5)
        appointment = Appointment.objects.create(doctor=doctor, 
                                                email='test2@mail.com',
                                                date=date)
        self.assertRaises(ValidationError, appointment.full_clean)


    def test_appointments_cant_be_at_same_time(self):
        doctor = Doctor.objects.get(pk=self.doctor_id)
        first_app = Appointment.objects.get(id=self.obj_id)
        date = first_app.date
        appointment = Appointment.objects.create(doctor=doctor, email='test@mail.com', date=date )
        self.assertFalse(appointment.full_clean())
    

    def test_status_choices(self):
        appointment = Appointment.objects.get(id=self.obj_id)
        appointment.status = 'cancelled'
        self.assertRaises(ValidationError, appointment.full_clean)
