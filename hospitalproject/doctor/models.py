from django.db import models
from  autoslug import AutoSlugField
from django.conf import settings



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
    old_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    next_available_day = models.CharField(max_length=100, blank=True, null=True, default="")
    next_available_time = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)
    


def __str__(self):
        return f"Dr. {self.name} ({self.speciality})"

