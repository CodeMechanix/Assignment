from django.db import models


class DoctorDetails(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PatientDetails(models.Model):
    patient_name = models.TextField()
    patient_address = models.TextField()

    doctor = models.ForeignKey('DoctorDetails', on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name
