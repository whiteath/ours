from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.context_processors import csrf
from django.contrib import auth

def home(request):
    re = {"name":"world"}
    if request.user.is_authenticated():
        re["name"] = request.user.get_username()

    return render(request,'index.html',re);

def user_login(request):
    '''It's aiming to handle the login scheme.

    Just return the user's info'''

    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'login.html',ctx)

def user_logout(request):
    auth.logout(request)
    return redirect('/')
