from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import User, Doctor
from django.utils import timezone


class UserTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(first_name='John', last_name='Doe',
                                   email='johndoe@mail.com', username='jonhdoe', password='pass')
        cls.id = user.id

    def test_user_is_active(self):
        user = User.objects.get(id=self.id)
        self.assertEquals(user.is_active, True)


class DoctorTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(first_name='John', last_name='Doe',
                                   email='johndoe@mail.com', username='jonhdoe', password='pass', is_doctor=True)
        doctor = Doctor.objects.get(user_id=user.id)
        cls.id = doctor.pk

    def test_user_is_doctor(self):
        doctor = Doctor.objects.get(pk=self.id)
        user = User.objects.get(id=doctor.user_id)
        self.assertEquals(user.is_doctor, True)
