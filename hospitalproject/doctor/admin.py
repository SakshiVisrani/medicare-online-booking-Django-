from django.contrib import admin
from .models import Doctor , Speciality ,Booking,AppointmentSlot 

# Register your models here.

# class DoctorAdmin(admin.ModelAdmin):
#     list_display=['id', 'doctor_name' , 'experience' , 'consultation_fees' , 'image', 'speciality']

# admin.site.register(Doctor,DoctorAdmin)


# class SpecialityAdmin(admin.ModelAdmin):
#     list_display=['id', 'speciality_name','slug']

# admin.site.register(Speciality,SpecialityAdmin)

admin.site.register(Doctor)
admin.site.register(Speciality)
admin.site.register(AppointmentSlot)
admin.site.register(Booking)
