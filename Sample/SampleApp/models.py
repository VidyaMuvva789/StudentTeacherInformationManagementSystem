from django.db import models
from django.contrib.auth.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    phone_number = models.CharField(max_length=15, default='000-000-0000')
    highest_degree = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class WorkExperience(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)
    worked_as = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.college_name} ({self.duration})"
