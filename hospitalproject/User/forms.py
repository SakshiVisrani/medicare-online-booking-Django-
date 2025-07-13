from django import forms
from django.contrib.auth.forms import UserCreationForm


# class DoctorRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = CustomUser
#         fields = ['doctor_name', 'speciality', 'location', 'current_workplace' , 'phone_number' ,'email']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.role = 'doctor'  
#         if commit:
#             user.save()
#         return user
