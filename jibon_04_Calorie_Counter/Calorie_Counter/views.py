from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileForm, DailyCalorieForm
from .models import UserProfile, DailyCalorie
from datetime import date


def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    profile = UserProfile.objects.get(user=request.user)
    today = date.today()
    daily_calories = DailyCalorie.objects.filter(user=request.user, date=today)


    total_consumed = sum(item.calories for item in daily_calories)


    if profile.gender == 'M':
        bmr = 66.47 + (13.75 * profile.weight_kg) + (5.003 * profile.height_cm) - (6.755 * profile.age)
    else:
        bmr = 655.1 + (9.563 * profile.weight_kg) + (1.850 * profile.height_cm) - (4.676 * profile.age)


    if request.method == 'POST':
        calorie_form = DailyCalorieForm(request.POST)
        if calorie_form.is_valid():
            new_calorie = calorie_form.save(commit=False)
            new_calorie.user = request.user
            new_calorie.save()
            return redirect('dashboard')
    else:
        calorie_form = DailyCalorieForm()

    return render(request, 'dashboard.html', {
        'profile': profile,
        'bmr': round(bmr, 2),
        'total_consumed': total_consumed,
        'daily_calories': daily_calories,
        'calorie_form': calorie_form
    })