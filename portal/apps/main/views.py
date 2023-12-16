from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def index_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        print(vars(request.user._wrapped))
    return render(request, "main/index.html")


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "You're now logged out.")
    return redirect("main:index")
