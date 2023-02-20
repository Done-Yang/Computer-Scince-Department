from django.shortcuts import render, redirect
from django.contrib import auth, messages
from app.models import Student

def home(request):
    return render(request, 'Student/home.html')