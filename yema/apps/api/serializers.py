from rest_framework import serializers
from ..appointment.models import Appointment
from ..users.models import Doctor, User


class AppointmentDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    class Meta:
        model = Appointment
        fields = ['email', 'status', 'date', 'time', 'doctor', 'comments']
        extra_kwargs = {
            'status': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ('user', 'pk')

    def create(self, validated_data):
        user = User.objects.create(**validated_data['user'])
        return Doctor.objects.create(user=user)
