from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
]
