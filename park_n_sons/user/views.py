from django.shortcuts import render
from user.forms import *
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django import forms


def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form, 'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form, 'user': request.user})
