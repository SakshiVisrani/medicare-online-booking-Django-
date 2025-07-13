from django.urls import path
from . import views
from .views import DoctorDetailView, SpecialityDetailView

urlpatterns = [
   path('', views.doctors, name='doctors'),
   path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
   path('speciality/<slug:slug>' ,SpecialityDetailView.as_view(),name='speciality-detail'),
]