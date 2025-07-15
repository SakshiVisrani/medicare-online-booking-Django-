from django.shortcuts import render, get_object_or_404
from .models import Doctor,Speciality
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time ,date
from .models import Doctor,DoctorAvailability


# Create your views here.
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors': doctors})


class DoctorDetailView(DetailView):
    model=Doctor
    template_name='doctor_detail.html'
    context_object_name='doctor'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



class SpecialityDetailView(DetailView):
    model=Speciality
    template_name="speciality.html"
    context_object_name="speciality"
    slug_field="slug"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["doctors"]=Doctor.objects.all()
        return context
    


def doctor_availability(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    today = date.today()
    days = [today + timedelta(days=i) for i in range(5)]  # Today to Friday

    date_slots = []
    for d in days:
        slots = DoctorAvailability.objects.filter(doctor=doctor, date=d, is_booked=False)
        date_slots.append({
        'date': d,
        'label': 'Today' if d == today else d.strftime('%A')[:3],  # Today, Mon, Tue...
        'slot_count': slots.count(),
        'slots': slots,
        })

    return render(request, 'doctor/availability.html', {
        'doctor': doctor,
        'date_slots': date_slots,
    })

def search_doctors(request):
    speciality_query = request.GET.get('speciality')
    location_query = request.GET.get('location')

    doctors = Doctor.objects.all()

    if speciality_query:
        doctors = doctors.filter(speciality__name__icontains=speciality_query)

    if location_query:
        doctors = doctors.filter(location__icontains=location_query)

    return render(request, 'search_results.html', {
        'doctors': doctors,
        'speciality_query': speciality_query,
        'location_query': location_query,
    })










    
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