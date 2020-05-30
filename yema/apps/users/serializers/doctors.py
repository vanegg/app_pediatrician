from rest_framework import serializers
from ..models import Doctor


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user', 'full_name', 'email')
