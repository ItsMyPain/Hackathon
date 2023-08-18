from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'lesnoy_elf'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ivanov@elflesnoy.ru'}),
        }
