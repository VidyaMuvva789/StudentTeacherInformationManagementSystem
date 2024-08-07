from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TeacherProfile, WorkExperience

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')

class TeacherRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    highest_degree = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'email', 'phone_number', 'highest_degree']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['full_name', 'email', 'phone_number', 'highest_degree']


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['duration', 'college_name', 'worked_as']
