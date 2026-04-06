from django.contrib import admin
from .models import UserProfile, DailyCalorie

admin.site.register(UserProfile)
admin.site.register(DailyCalorie)