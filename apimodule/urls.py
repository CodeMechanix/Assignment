from django.urls import path

from .views import DoctorDetailsAPIView, PatientDetailsAPIView, PatientDetailsAPIDetailView, \
    PatientDetailsAPINewView

urlpatterns = [
    path('', DoctorDetailsAPIView.as_view()),
    path('patients/', PatientDetailsAPIView.as_view()),
    path('patients/<int:pk>/', PatientDetailsAPIDetailView.as_view()),
    path('patients/add/', PatientDetailsAPINewView.as_view()),
]
