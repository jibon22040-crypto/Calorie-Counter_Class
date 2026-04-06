from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, DailyCalorie
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'height_cm', 'weight_kg']

class DailyCalorieForm(forms.ModelForm):
    class Meta:
        model = DailyCalorie
        fields = ['item_name', 'calories']