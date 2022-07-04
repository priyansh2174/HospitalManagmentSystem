# Generated by Django 4.0.5 on 2022-06-29 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_doctors_options_alter_patients_options'),
        ('hospital', '0009_alter_doctortimeslots_doctor_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='doctor_time_slots',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.doctortimeslots'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.patients'),
        ),
        migrations.AlterField(
            model_name='doctorservices',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.doctors'),
        ),
        migrations.AlterField(
            model_name='doctorservices',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.services'),
        ),
        migrations.AlterField(
            model_name='doctortimeslots',
            name='doctor_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.doctorservices'),
        ),
    ]
