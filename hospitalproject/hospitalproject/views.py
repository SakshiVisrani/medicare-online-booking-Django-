from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
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


def register(request):
    if request.method == "GET":
        return render(request, "signin.html")
    elif request.method == "POST":
        print("POST request")

        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordconfirmation = request.POST.get("confirm_password")
        
        if password != passwordconfirmation:
            message = "Passwords do not match"
            return render(request, "signin.html", {"message": message})
        
        user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_active=True
        )
        message = "Registered Successful"
        return render(request, "signin.html", {"message": message})
    

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