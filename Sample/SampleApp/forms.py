from django import forms
from .models import TeacherProfile, WorkExperience

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['full_name', 'dob', 'highest_degree']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['duration', 'college_name', 'worked_as']