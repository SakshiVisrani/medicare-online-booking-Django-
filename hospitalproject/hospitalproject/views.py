from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from doctor.models import Doctor, AppointmentSlot, Booking
User = get_user_model()


def home(request):
    return render(request,'index.html')      

def doctor(request):
    return render(request , 'doctor.html')

def patient(request):
    return render (request , 'patient.html')

def contact(request):
    return render (request , 'contact.html')

def signin(request):
    return render (request, 'signin.html')

def health_plans(request):
    return render (request , 'health_plans.html')

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def payment_success(request):
    data = request.session.get('booking_data')
    if not data:
        return redirect('doctors')  # or show error

    doctor = Doctor.objects.get(id=data['doctor_id'])
    slot = AppointmentSlot.objects.get(id=data['slot_id'])

    # Mark slot as booked
    slot.is_booked = True
    slot.save()

    # Create Booking
    Booking.objects.create(
        doctor=doctor,
        user=request.user,
        slot=slot
    )

    del request.session['booking_data']  # clean session
    return render(request, 'payment_success.html')



def register(request):
    if request.method == "GET":
        print("asdfghjk")
        return render(request, "signin.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordconfirmation = request.POST.get("confirm_password")

        if password != passwordconfirmation:
            message = "Passwords do not match"
            return render(request, "signin.html", {"message": message})

        if User.objects.filter(username=username).exists():
            return render(request, "signin.html", {"message": "Username already taken."})
        if User.objects.filter(email=email).exists():
            return render(request, "signin.html", {"message": "Email already registered."})

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_active=True
        )

        message = "Registration Successful. Please sign in."
        return redirect("login")

def user_login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("Username:", username)
        print("Password:", password)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        print("User exists:", User.objects.filter(username=username).exists())
        user = authenticate(request, username=username, password=password)
        message = None
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        message = "Login Failed"
        return render(request, "login.html", {"message": message})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")