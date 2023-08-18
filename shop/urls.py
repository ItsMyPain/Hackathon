from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("registration/", views.RegisterUser.as_view(), name="registration"),
]
