from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1, "HOD"),
        (2, "OFFICER"),
        (3, "TEACHER"),
        (4, "STUDENT")
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to="media/profile_pic")

class SessionYear(models.Model):
    sessionYear = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sessionYear
    
class Officer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    officerID = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacherID = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    sessionYearID = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    year = models.CharField(max_length=30)
    part = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    year = models.CharField(max_length=30)
    teacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    sessionYearID = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

