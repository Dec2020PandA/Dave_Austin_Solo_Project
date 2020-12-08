from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, "index.html")


def log_in(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("/select")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        if not (
            User.objects.filter(username=request.POST["username"])
            or User.objects.filter(username=request.POST["email"])
        ):
            login(
                request,
                User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password"],
                ),
            )
            return redirect("/select")

    return render(request, "register.html")


def select(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, "select.html")
    return redirect("/")


def learn(request):
    return render(request, "learn.html")


def test(request):
    return render(request, "test.html")
