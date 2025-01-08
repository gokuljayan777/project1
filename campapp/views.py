from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html')

def pogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if not user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'okeyyyyyyyyyy')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')

        user = User(username=username, email=email, password=make_password(password))
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')

def college(request):
    return render(request, 'college.html')

def course(request):
    return render(request, 'course.html')

def contact(request):
    return render(request, 'contact.html')
