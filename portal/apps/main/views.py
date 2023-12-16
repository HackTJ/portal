from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/logout.html")
