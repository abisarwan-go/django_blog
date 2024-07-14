# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from authentication.forms import RegistrationForm
from django.http import JsonResponse

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    request.disable_login = True
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/authentication.html', {
                'form': form,
                'errors': form.errors,
                'show_register': True})
    else:
        form = RegistrationForm()
    return render(request, "authentication/authentication.html", {'form': form})

def login_view(request):
    request.disable_login = True
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('/')  # Redirect to a home page or another page of your choice
        else:
            return render(request, "authentication/authentication.html", {'form': form, 'errors': form.errors})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/authentication.html', {'form': form})

def authentication_view(request):
    request.disable_login = True
    return render(request, 'authentication/authentication.html')

