from django.db import models
from  autoslug import AutoSlugField
from django.conf import settings
from datetime import time, date
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=100, unique=True , default="")

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100 , default="")
    image = models.ImageField(upload_to='doctor_images/', default='default.jpg')
    experience = models.IntegerField(help_text="Years of experience" , default="")
    location = models.CharField(max_length=100 , default="")
    clinic_name = models.CharField(max_length=100, blank=True, null=True, default="")
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='doctors', default="")
    response_time = models.IntegerField(help_text="Responds in how many minutes", null=True, blank=True, default="")
    consultation_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    online_consultation=models.DecimalField(max_digits=6 , decimal_places=2 , null=True, blank=True)
    platform_fee=models.DecimalField(max_digits=6, decimal_places=2 , null=True, blank=True)
    old_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    next_available_day = models.CharField(max_length=100, blank=True, null=True, default="")
    next_available_time = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)

    
    
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True , default="")  


def __str__(self):
        return f"Dr. {self.name} ({self.speciality} {self.location})"


class DoctorAvailability(models.Model):
     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="availabilities")
     date=models.DateField()
     time=models.TimeField()
     is_booked=models.BooleanField(default=False)

     class Meta:
          unique_together = ('doctor', 'date', 'time')
          ordering = ['date', 'time']

     def __str__(self):
        return f"{self.doctor.name} - {self.date} at {self.time}"

class Appointment(models.Model):
    
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    CONSULTATION_TYPES = [
        ('clinic_visit', 'Clinic Visit'),
        ('video_call', 'Video Call'),
    ]
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPES, default='clinic_visit')
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.patient.username} with Dr. {self.doctor.name} on {self.date} at {self.time}"

