from rest_framework import serializers

from patientmodule.models import PatientDetails
from patientmodule.models import DoctorDetails


class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'


class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = '__all__'
