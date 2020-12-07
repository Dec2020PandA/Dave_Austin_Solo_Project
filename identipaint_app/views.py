from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def select(request):
    return render(request, "select.html")


def learn(request):
    return render(request, "learn.html")
