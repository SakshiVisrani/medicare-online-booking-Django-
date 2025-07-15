from django.shortcuts import render, get_object_or_404
from .models import Doctor,Speciality
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time ,date
from .models import Doctor,DoctorAvailability,Appointment
from django.http import JsonResponse


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.filter(doctor=self.object).order_by('date', 'time')
        return context



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


def book_slot(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        date_str = request.POST.get('date')         # Format: YYYY-MM-DD
        time_str = request.POST.get('time')         # Format: HH:MM
        consultation_type = request.POST.get('consultation_type')  # 'clinic_visit' or 'video_call'

        doctor = get_object_or_404(Doctor, id=doctor_id)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        time_obj = datetime.strptime(time_str, '%H:%M').time()

        # Set consultation fee based on type
        if consultation_type == 'clinic_visit':
            consultation_fee = doctor.consultation_fee
        elif consultation_type == 'video_call':
            consultation_fee = doctor.online_consultation
        else:
            return JsonResponse({'success': False, 'error': 'Invalid consultation type'}, status=400)

        platform_fee = doctor.platform_fee or 50
        tax = 0.18 * (consultation_fee + platform_fee)
        total = consultation_fee + platform_fee + tax

        # Save appointment
        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=request.user,
            date=date_obj,
            time=time_obj,
            consultation_type=consultation_type,
            consultation_fee=consultation_fee,
            platform_fee=platform_fee,
            total=total
        )

        # Define all available slots
        all_slots = [
            time(9, 0), time(10, 0), time(11, 0),
            time(12, 0), time(14, 0), time(15, 0),
            time(16, 0), time(17, 0), time(18, 0)
        ]

        try:
            current_index = all_slots.index(time_obj)
            next_slot = all_slots[current_index + 1]
        except (ValueError, IndexError):
            next_slot = None

        return JsonResponse({
            'success': True,
            'next_slot': next_slot.strftime('%I:%M %p') if next_slot else 'No more slots today',
            'consultation_fee': consultation_fee,
            'platform_fee': platform_fee,
            'tax': round(tax),
            'total': round(total)
        })

    return JsonResponse({'success': False}, status=400)







    
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