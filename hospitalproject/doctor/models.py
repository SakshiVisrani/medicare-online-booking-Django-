from django.db import models
from  autoslug import AutoSlugField
from django.conf import settings
from datetime import time, date
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.contrib.auth.models import User
import calendar
User = get_user_model()


# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)  # <--- important

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='doctor_images/', default='default.jpg')
    experience = models.IntegerField(help_text="Years of experience", default=0)
    location = models.CharField(max_length=100, default="")
    clinic_name = models.CharField(max_length=100, blank=True, null=True, default="")
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, related_name='doctors', default="")
    response_time = models.IntegerField(help_text="Responds in how many minutes", null=True, blank=True, default=0)
    consultation_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    online_consultation = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    platform_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    old_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    next_available_day = models.CharField(max_length=100, blank=True, null=True, default="")
    next_available_time = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)

    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    patients_treated = models.PositiveIntegerField(default=0)

    education_1 = models.CharField("Education 1", max_length=255, blank=True, null=True)
    education_2 = models.CharField("Education 2", max_length=255, blank=True, null=True)
    education_3 = models.CharField("Education 3", max_length=255, blank=True, null=True)
    education_4 = models.CharField("Education 4", max_length=255, blank=True, null=True)

    slug = AutoSlugField(populate_from='name', unique=True, always_update=True, default="")

    def __str__(self):
        return f"Dr. {self.name} ({self.speciality} - {self.location})"
# DAYS_OF_WEEK = [
#     ('Monday', 'Monday'),
#     ('Tuesday', 'Tuesday'),
#     ('Wednesday', 'Wednesday'),
#     ('Thursday', 'Thursday'),
#     ('Friday', 'Friday'),
#     ('Saturday', 'Saturday'),
#     ('Sunday', 'Sunday'),
# ]


# class DoctorAvailability(models.Model):
#     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="availabilities")
#     day = models.CharField(choices=DAYS_OF_WEEK, max_length=10 , default="")
#     date=models.DateField()
#     time=models.TimeField()
#     is_booked=models.BooleanField(default=False)
#     class Meta:
#         unique_together = ('doctor', 'date', 'time')
#         ordering = ['date', 'time']

#     def __str__(self):
#         return f"{self.doctor.name} - {self.date} at {self.time} on {self.day}"
     

class AppointmentSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('doctor', 'date', 'time')
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.date} - {self.time} ({'Booked' if self.is_booked else 'Available'})"
    @property
    def day_name(self):
        return calendar.day_name[self.date.weekday()]
class Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(AppointmentSlot, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

# class Appointment(models.Model):
    
#     patient = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()

#     CONSULTATION_TYPES = [
#         ('clinic_visit', 'Clinic Visit'),
#         ('video_call', 'Video Call'),
#     ]
#     consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPES, default='clinic_visit')
#     consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
#     total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.patient.username} with Dr. {self.doctor.name} on {self.date} at {self.time}"


