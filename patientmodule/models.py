from django.db import models
from django.utils import timezone

import datetime

class DoctorDetails(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class PatientDetails(models.Model):
    patient_name = models.TextField()
    patient_address = models.TextField()

    doctor = models.ForeignKey('DoctorDetails', on_delete=models.CASCADE)

    publishing_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
    )
    # Set TTL for Five Minutes
    @property
    def delete_after_five_minutes(self):
        time = self.publishing_date + datetime.timedelta(minutes=5)
        if time < datetime.datetime.now():
            e = PatientDetails.objects.get(pk=self.pk)
            e.delete()
            return True
        else:
            return False

    def __str__(self):
        return self.patient_name
