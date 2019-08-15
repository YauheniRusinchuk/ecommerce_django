from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login

def login(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('home:login:login_page')
    if request.user.is_authenticated:
        return redirect('home:home_page')
    return render(request, 'auth/login.html', {})
