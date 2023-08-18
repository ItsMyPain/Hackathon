from secrets import compare_digest

from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from shop.models import User


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '111111'}), label='Повтор пароля')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Эльф'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Лесной'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ivanov@elflesnoy.ru'}),
            'password': forms.PasswordInput(attrs={'placeholder': '111111'})
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and not compare_digest(password, password2):
            raise ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'ivan@mail.ru'}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '111111'}))
