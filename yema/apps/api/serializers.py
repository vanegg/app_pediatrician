from rest_framework import serializers
from ..appointment.models import Appointment
from ..users.models import Doctor, User


class AppointmentDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    class Meta:
        model = Appointment
        fields = ['email', 'status', 'date', 'time', 'doctor']
        extra_kwargs = {
            'status': {
                'read_only': True
            }
        }

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Doctor
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
