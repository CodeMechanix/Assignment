# Generated by Django 3.0.1 on 2019-12-29 16:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.TextField()),
                ('patient_address', models.TextField()),
                ('publishing_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmodule.DoctorDetails')),
            ],
        ),
    ]
