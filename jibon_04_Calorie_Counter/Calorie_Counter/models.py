from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES,null=True)
    height_cm = models.FloatField(null=True)
    weight_kg = models.FloatField(null=True)

    def __str__(self):
        return self.user.username

class DailyCalorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    item_name = models.CharField(max_length=100,null=True)
    calories = models.FloatField(null=True)

    def __str__(self):
        return f"{self.item_name} - {self.calories}"