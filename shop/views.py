from django.http import HttpResponse
from django.template import loader

from .forms import LoginFrom


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
    print(request.GET)
    print(request.POST)
    template = loader.get_template("shop/registration.html")
    context = {}
    return HttpResponse(template.render(context, request))
