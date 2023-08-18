from django.contrib import admin

from .forms import RegistrationForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at', 'updated_at']
    form = RegistrationForm
