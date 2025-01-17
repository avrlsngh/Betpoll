from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from matches.models import UserRight

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_right = UserRight()
        if form.is_valid():
            user = form.save()
            user_right.user = user
            user_right.save()
            login(request, user)
            # log the user in
            return redirect('matches:viewMatches')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('matches:viewMatches')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')