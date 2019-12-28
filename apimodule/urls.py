from django.urls import path

from .views import DoctorDetailsAPIView, PatientDetailsAPIView, PatientDetailsAPIDetailView, \
    PatientDetailsAPINewView

urlpatterns = [
    path('', DoctorDetailsAPIView.as_view()),
    path('all-patients/', PatientDetailsAPIView.as_view()),
    path('patient/<int:pk>/', PatientDetailsAPIDetailView.as_view()),
    path('patient/add/', PatientDetailsAPINewView.as_view()),
]
