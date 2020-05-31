from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class AppointmentValidator:
    def validate_future_date(self, value):
        if value <= timezone.now().date():
            raise ValidationError(
                _('%(value)s date_future'),
                params={'value': value},
            )