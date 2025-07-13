from django.shortcuts import render
from .models import Doctor,Speciality
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time
from .models import Doctor


# Create your views here.
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors': doctors})


class DoctorDetailView(DetailView):
    model=Doctor
    template_name='doctor_detail.html'
    context_object_name='doctor'


class SpecialityDetailView(DetailView):
    model=Speciality
    template_name="speciality.html"
    context_object_name="speciality"
    slug_field="slug"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["doctors"]=Doctor.objects.all()
        return context
    
# def generate_slots_for_doctors(doctor_id):
#     doctor = Doctor.objects.get(id=doctor_id)
#     now = datetime.now().date()

#     morning_times = [time(10, 0), time(10, 15), time(10, 30), time(10, 45),
#                      time(11, 0), time(11, 15), time(11, 30), time(11, 45)]
#     afternoon_times = [time(12, 0), time(12, 15), time(12, 30), time(12, 45),
#                        time(13, 0), time(13, 15), time(13, 30), time(13, 45),
#                        time(14, 0)]
    
#     for day in range(10):
#         date = now + timedelta(days=day)
#         for t in morning_times + afternoon_times:
#             TimeSlot.objects.get_or_create(doctor=doctor, date=date, time=t)
    

# def doctor_register(request):
#     if request.method=='POST':
#         user_form=DoctorRegisterForm(request.POST)
#         if user_form.is_valid():
#             user=user_form.save()

#             return redirect('doctor')
 
#         else:
#             user_form = DoctorRegisterForm()

#         return render(request,'doctor.html', {'user_form' : user_form})