from django.urls import path 
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
from .views import book_slot, DoctorDetailView, SpecialityDetailView, doctor_availability, search_doctors,doctors_by_speciality,book_appointment,doctors
from .views import payment_success
urlpatterns = [
   path('doctors/', doctors, name='doctors'),
   path('doctor/<slug:slug>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/<slug:slug>/availability/', doctor_availability, name='doctor-availability'),
   path('book-slot/<slug:slug>/<int:slot_id>', book_slot, name='book-slot'),  # ✅ Corrected
   # path('speciality/<slug:slug>/', SpecialityDetailView.as_view(), name='speciality-detail'),
   path('search/', search_doctors, name='search-doctors'),
    path('speciality/<str:speciality_slug>/',doctors_by_speciality, name='doctors_by_speciality'),
   path('book/<int:slot_id>/', book_appointment, name='book-appointment'),
   path('payment/success/', payment_success, name='payment-success'),

]
