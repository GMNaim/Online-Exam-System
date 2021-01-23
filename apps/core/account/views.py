from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout as auth_logout


def registration(request):
    return render(request, 'account/registration.html')


def login(request):
    if request.user.is_authenticated:
        # anonymity and redirection is checked in middleware
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, 'account/login.html')


def logout(request):
    auth_logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


def reset(request):
    return render(request, 'account/reset.html')


def change_password(request):
    return render(request, 'account/change_password')
