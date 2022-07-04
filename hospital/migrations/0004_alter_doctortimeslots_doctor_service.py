# Generated by Django 4.0.5 on 2022-06-23 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_appointments_booking_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortimeslots',
            name='doctor_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.doctorservices'),
        ),
    ]
