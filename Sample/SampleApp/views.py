from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import TeacherRegistrationForm, TeacherProfileForm, WorkExperienceForm, EmailForm
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

    work_experience_form = WorkExperienceForm()
    work_experiences = WorkExperience.objects.filter(teacher=profile)

    return render(request, 'profile.html', {
        'profile': profile,
        'work_experience_form': work_experience_form,
        'work_experiences': work_experiences
    })

@login_required
def edit_profile(request):
    try:
        profile = TeacherProfile.objects.get(user=request.user)
    except TeacherProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        profile_form = TeacherProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = TeacherProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {
        'profile_form': profile_form
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
    else:
        work_experience_form = WorkExperienceForm()

    return render(request, 'add_work_experience.html', {
        'work_experience_form': work_experience_form
    })

@login_required
def edit_work_experience(request, id):
    work_experience = get_object_or_404(WorkExperience, id=id)
    if request.method == 'POST':
        work_experience_form = WorkExperienceForm(request.POST, instance=work_experience)
        if work_experience_form.is_valid():
            work_experience_form.save()
            return redirect('profile')
    else:
        work_experience_form = WorkExperienceForm(instance=work_experience)

    return render(request, 'edit_work_experience.html', {
        'work_experience_form': work_experience_form
    })

@login_required
def delete_work_experience(request, id):
    work_experience = get_object_or_404(WorkExperience, id=id)
    if request.method == 'POST':
        work_experience.delete()
        return redirect('profile')
    return render(request, 'delete_work_experience.html', {
        'work_experience': work_experience
    })
