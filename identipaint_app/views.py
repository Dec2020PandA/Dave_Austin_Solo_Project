import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .services import get_paintings, get_artists, new_session
from .models import CardStack, Artist, Painting

# from django.contrib import messages


def index(request):
    return render(request, "index.html")


def log_in(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            request.session["session_key"] = new_session(request)
            print(request.session["session_key"])
            return redirect("/select")
        else:
            pass

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

    artists = get_artists(request.session["session_key"])["data"]

    new_stack = CardStack.objects.create()

    for _i in range(5):
        idx = random.randint(0, len(artists) - 1)
        if Artist.objects.filter(id=artists[idx]["id"]):
            if new_stack.artists.filter(id=artists[idx]["id"]):
                _i -= 1
            else:
                new_stack.artists.add(Artist.objects.get(id=artists[idx]["id"]))
        else:
            new_stack.artists.add(
                Artist.objects.create(
                    id=artists[idx]["id"],
                    name=artists[idx]["artistName"],
                    url=artists[idx]["url"],
                )
            )

    for artist in new_stack.artists.all():

        paintings = get_paintings(artist.url, request.session["session_key"])

        study_i = random.randint(0, len(paintings) - 1)
        test_i = study_i
        while test_i == study_i:
            test_i = random.randint(0, len(paintings) - 1)

        add_paintings = [
            {"idx": paintings[study_i], "stack": new_stack.study_paintings},
            {"idx": paintings[test_i], "stack": new_stack.test_paintings},
        ]

        for i in add_paintings:
            if Painting.objects.filter(id=i["idx"]["contentId"]):
                i["stack"].add(Painting.objects.get(id=i["idx"]["contentId"]))
            else:
                i["stack"].add(
                    Painting.objects.create(
                        id=i["idx"]["contentId"],
                        title=i["idx"]["title"],
                        artist=artist,
                        image_url=i["idx"]["image"].split("!")[0],
                    )
                )

    context = {"cardstack_id": new_stack.id, "stack": new_stack.study_paintings}

    return render(request, "learn.html", context)


def test(request):
    if request.method == "POST":
        stack = CardStack.objects.get(id=request.POST["stack"])
        context = {"stack": stack.test_paintings, "artists": stack.artists}
        return render(request, "test.html", context)
