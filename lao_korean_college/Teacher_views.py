from django.shortcuts import render, redirect
from django.contrib import auth, messages
from app.models import Teacher

def home(request):
    return render(request, 'Teacher/home.html')