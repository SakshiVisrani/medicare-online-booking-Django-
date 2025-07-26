"""
URL configuration for hospitalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.urls import include
from . import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
   
    path('register/doctor',views.doctor,name='doctor'),
    path('register/patient',views.patient,name='patient'),
    path('contact',views.contact,name='contact'),
    path('', include('doctor.urls')),
    path('login',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signin/' ,views.register, name='signin'),
    path('health_plans/' , views.health_plans , name='health_plans'),
    path('about/', views.about , name='about'),
    path('payment-success/', views.payment_success, name='payment_success'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
