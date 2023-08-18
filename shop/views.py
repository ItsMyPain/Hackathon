from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


def main_page(request):
    template = loader.get_template("shop/main_page.html")
    context = {}
    return HttpResponse(template.render(context, request))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'shop/registration.html'
    success_url = reverse_lazy('main_page')
