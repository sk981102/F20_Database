from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            #user_instance.generate()
            user_instance.set_password(form.cleaned_data['PW'])
            user_instance.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['PW']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def viewusers(request):
    candidates = UserProfile.objects.all()
    context = {'candidates' : candidates}
    return render(request, 'viewusers.html', context)

def myaccount(request):
    form = get_object_or_404(UserProfile, pk=request.user.pk)
    return render(request, 'myaccount.html', {'form': form})
"""
def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepw,html', {'form': form})
"""