from django.test import TestCase
from ..models import Appointment
from django.utils import timezone

class AppointmentTest(TestCase):
     def setUp(self):
        Appointment.objects.create(doctor="lion", sound="roar")
        Appointment.objects.create(name="cat", sound="meow")

    def test_appointments_can_speak(self):
        """Appointments that can speak are correctly identified"""
        lion = Appointment.objects.get(name="lion")
        cat = Appointment.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
