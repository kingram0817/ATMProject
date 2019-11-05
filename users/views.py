from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def myAccount(request):
    return render(request, 'myAccount.html', {})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in - Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Thank you for registering')
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context)
