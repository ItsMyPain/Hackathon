from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from .forms import RegistrationForm


def main_page(request):
    template = loader.get_template("shop/base.html")
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'POST':
        user = LoginFrom(request.POST)
    else:
        user = LoginFrom()
    print(user)
    template = loader.get_template("shop/login.html")
    context = {'user': user}
    return HttpResponse(template.render(context, request))


def registration(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('main_page')
    else:
        reg_form = RegistrationForm()

    template = loader.get_template("shop/registration.html")
    context = {'form': reg_form}
    return HttpResponse(template.render(context, request))
