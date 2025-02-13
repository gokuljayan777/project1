from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import*
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def pogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
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

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')

def college_list(request):
    colleges = College.objects.all()  # Fetch all colleges
    return render(request, 'college_list.html', {'colleges': colleges})


def course(request):
    return render(request, 'course.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    return render(request, 'quiz_result.html')




def quiz_view(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        user_answers = request.POST
        scores = {'Verbal Ability': 0, 'Analytical Ability': 0, 'Numerical Ability': 0}

        for question in questions:
            user_answer = user_answers.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                scores[question.category] += 1

        result, created = QuizResult.objects.get_or_create(user=request.user)
        result.Verbal_score = scores['Verbal Ability']
        result.Analytical_score = scores['Analytical Ability']
        result.Numerical_score = scores['Numerical Ability']
        result.determine_course()

        return redirect('quiz_result')
    questions = Question.objects.order_by('category', 'text')  # Sorting by category first, then text
    return render(request, 'quiz_page.html', {'questions': questions})

def quiz_result(request):
    result = QuizResult.objects.get(user=request.user)  # Fetch user's quiz result

    return render(request, 'quiz_result.html', {'result': result})
def stc(request):
    return render(request, 'stc.html')

