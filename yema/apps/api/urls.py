from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'doctors', views.DoctorList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^doctors/(?P<id>\d+)$',
        views.DoctorDetail, name='doctor-detail'),
    url(r'^doctors/$',
        views.DoctorList, name='doctor-list'),
]
