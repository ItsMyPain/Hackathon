from django import forms


class LoginFrom(forms.Form):
    email = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'ivan@mail.ru'}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '111111'}))
