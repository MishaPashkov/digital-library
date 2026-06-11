from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            form.add_error("username", "Користувач з таким логіном вже існує")
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm(request.POST)
    return render(request, "accounts/register.html", {"form": form})


def check_username(request):
    username = request.GET.get("username")

    exists = User.objects.filter(username=username).exists()

    return JsonResponse({
        "exists": exists
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")