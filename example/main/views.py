from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'main/login.html', context)


def navigate(request):
    context = {}
    return render(request, 'main/navigate.html', context)


def open_button(request):
    context = {}
    return render(request, 'main/open_button.html', context)


def links_login(request):
    context = {}
    return render(request, 'main/links_login.html', context)
