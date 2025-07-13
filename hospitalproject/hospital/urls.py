from django.urls import path 
from . import views

urlpatterns = [
    path('',views.doctor,name='doctor'),
    path('<int:pk>', views.doctor_detail, name='doctor_detail'),
]
