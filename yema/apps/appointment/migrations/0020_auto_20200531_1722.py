# Generated by Django 3.0.6 on 2020-05-31 22:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import yema.apps.appointment.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200531_1722'),
        ('appointment', '0019_auto_20200530_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'appointment', 'verbose_name_plural': 'appointments'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='comments'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[yema.apps.appointment.validators.AppointmentValidator.validate_future_date], verbose_name='appointment_date'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor_user', to='users.Doctor', verbose_name='doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='appointment_hour'),
        ),
    ]
