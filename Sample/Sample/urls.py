"""
URL configuration for Sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
#from SampleApp import views 
# #from . import views
from SampleApp.views import send_email,profile_view, add_work_experience,edit_profile,edit_work_experience,delete_work_experience

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', send_email, name='send_email'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/work_experience/add/', add_work_experience, name='add_work_experience'),
    path('profile/work_experience/edit/<int:id>/', edit_work_experience, name='edit_work_experience'),
    path('profile/work_experience/delete/<int:id>/', delete_work_experience, name='delete_work_experience'),
    path('auth/', include("SampleApp.urls")),
]
