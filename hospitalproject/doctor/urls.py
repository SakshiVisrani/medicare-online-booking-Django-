from django.urls import path
from . import views
from .views import DoctorDetailView, SpecialityDetailView , doctor_availability ,search_doctors , book_slot

urlpatterns = [
   path('', views.doctors, name='doctors'),
   path('doctor/<slug:slug>/', DoctorDetailView.as_view(), name='doctor-detail'),
   path('doctor/<slug:slug>/availability/', doctor_availability, name='doctor-availability'),
   path('speciality/<slug:slug>' ,SpecialityDetailView.as_view(),name='speciality-detail'),
   path('search/', search_doctors, name='search-doctors'),
   path('book-slot/', book_slot, name='book-slot')
]