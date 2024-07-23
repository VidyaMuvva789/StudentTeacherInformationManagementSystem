from django.shortcuts import render,redirect
# Create your views here.
from django.core.mail import send_mail
from .forms import EmailForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import TeacherProfileForm, WorkExperienceForm
from .models import TeacherProfile, WorkExperience

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail(
                'Job alerts !!!',
                'New internship offer for Data science roles click here to register ',
                'your gmail',  # Sender's email address
                [email],  # Recipient's email address
                fail_silently=False,
            )
            return render(request, 'email_form.html')
    else:
        form = EmailForm()
    return render(request, 'email_form.html', {'form': form})

def teach_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})

def teach_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request,'auth/login.html',{'form':form})


def dashboard_view(request):
    return render(request,'base.html')

def teach_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    try:
        profile = TeacherProfile.objects.get(user=request.user)
    except TeacherProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        profile_form = TeacherProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            teacher_profile = profile_form.save(commit=False)
            teacher_profile.user = request.user
            teacher_profile.save()
            return redirect('profile')
    else:
        profile_form = TeacherProfileForm(instance=profile)

    work_experience_form = WorkExperienceForm()
    work_experiences = WorkExperience.objects.filter(teacher=profile)

    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'work_experience_form': work_experience_form,
        'profile': profile,
        'work_experiences': work_experiences
    })

@login_required
def add_work_experience(request):
    if request.method == 'POST':
        work_experience_form = WorkExperienceForm(request.POST)
        if work_experience_form.is_valid():
            work_experience = work_experience_form.save(commit=False)
            work_experience.teacher = TeacherProfile.objects.get(user=request.user)
            work_experience.save()
            return redirect('profile')
    return redirect('profile')
