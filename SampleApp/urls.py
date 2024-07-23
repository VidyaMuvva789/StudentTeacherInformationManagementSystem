from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.teach_register,name='register'),
    path('login/',views.teach_login,name='login'),
    path('logout/',views.teach_logout,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
]
