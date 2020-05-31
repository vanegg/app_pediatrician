from rest_framework import generics, status, viewsets
from .serializers import DoctorSerializer, AppointmentDetailSerializer, UserSerializer
from yema.apps.appointment.models import Appointment
from yema.apps.users.models import Doctor, User


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date', 'time')
    serializer_class = AppointmentDetailSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset


class DoctorList(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('user')
    serializer_class = DoctorSerializer


class DoctorDetail(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
