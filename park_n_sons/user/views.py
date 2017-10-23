from django.shortcuts import render
from user.forms import *
from django.contrib.auth import login as login_auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.models import User, Group


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            userType = form.cleaned_data.get('UserType')
            if userType == "bsns":
                group = Group.objects.get(name="Businessmen")
                user.groups.add(group)
            elif userType == "trst":
                group = Group.objects.get(name="Tourists")
                user.groups.add(group)
            elif userType == "sdnt":
                group = Group.objects.get(name="Students")
                user.groups.add(group)
            return redirect('index')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form, 'user': request.user})

def logout(request):
    logout_auth(request)
    return redirect('index')
