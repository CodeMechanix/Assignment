from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from patientmodule.models import PatientDetails, DoctorDetails
from .serializers import PatientDetailsSerializer, DoctorDetailsSerializer


class PatientDetailsAPIView(generics.ListAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer


class PatientDetailsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer


class PatientDetailsAPINewView(generics.ListCreateAPIView):
    queryset = ''  # latest quote
    serializer_class = PatientDetailsSerializer


class DoctorDetailsAPIView(generics.ListAPIView):
    queryset = DoctorDetails.objects.all()
    serializer_class = DoctorDetailsSerializer
