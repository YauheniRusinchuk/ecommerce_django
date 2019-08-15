from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/home.html', {})


@login_required(login_url="home:login:login_page")
def addnew(request):
    if request.user.is_authenticated:
        return render(request, 'addnew/new.html', {})
    return redirect('home:home_page')
