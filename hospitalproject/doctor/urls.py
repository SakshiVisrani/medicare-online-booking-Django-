from django.urls import path 
from . import views
from .views import DoctorDetailView, SpecialityDetailView , doctor_availability ,search_doctors , book_slot

# urlpatterns = [
    
#    path('', views.doctors, name='doctors'),
#    path('doctor/<slug:slug>/', DoctorDetailView.as_view(), name='doctor-detail'),
#    path('doctor/<slug:slug>/availability/', doctor_availability, name='doctor-availability'),
#    path('speciality/<slug:slug>' ,SpecialityDetailView.as_view(),name='speciality-detail'),
#    path('search/', search_doctors, name='search-doctors'),
#    path('doctors/book-slot/<slug:slug>/', views.book_slot, name='book-slot'),
#    path('doctors/speciality/<str:speciality_slug>/', views.doctors_by_speciality, name='doctors_by_speciality')
# ]


from django.urls import path
from .views import book_slot, DoctorDetailView, SpecialityDetailView, doctor_availability, search_doctors

urlpatterns = [
  path('book-slot/<slug:slug>/', book_slot, name='book-slot'),  # ✅ Corrected
    path('doctors/', views.doctors, name='doctors'),
    path('doctor/<slug:slug>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/<slug:slug>/availabsility/', doctor_availability, name='doctor-availability'),
    path('speciality/<slug:slug>', SpecialityDetailView.as_view(), name='speciality-detail'),
    path('search/', search_doctors, name='search-doctors'),
    path('speciality/<str:speciality_slug>/', views.doctors_by_speciality, name='doctors_by_speciality'),
]
