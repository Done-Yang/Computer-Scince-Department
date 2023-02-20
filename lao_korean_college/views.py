from django.shortcuts import render, redirect
from django.contrib import auth, messages
from app.EmailBackEnd import EmailBackEnd

def login(request):
    return render(request, 'login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
        username=request.POST.get('username'),
        password=request.POST.get('password'),)
    if user!=None:
        auth.login(request, user)
        user_type = user.user_type
        if user_type == '1':
            return redirect('hod_home')
        elif user_type == '2':
            return redirect('hod_home')
        elif user_type == '3':
            return redirect('teacher_home')
        elif user_type == '4':
            return redirect('student_home')
        else:
            messages.error(request, 'Email and Password are invalid!')
            return redirect('login')
    else:
        messages.error(request, 'Email and Password are invalid!')
        return redirect('login')

def dologout(request):
    auth.logout(request)
    return redirect('login')

