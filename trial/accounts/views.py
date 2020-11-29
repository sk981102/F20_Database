from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, CheckPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
#from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.hashers import check_password
from django.urls import path
from django.db.models import Q
from submitter.models import Submitter
from task.models import ApplyTask
from rater.models import Rater
from parsed_data.models import ParsedData

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            #user_instance.generate()
            user_instance.set_password(form.cleaned_data['PW'])
            user_instance.save()
            return redirect('signin')
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

def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepw.html', {'form': form})

def changeinfo(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.username = request.POST["username"]
        user.birthdate = request.POST["birthdate"]
        user.phone = request.POST["phone"]
        user.address = request.POST["address"]
        user.gender = request.POST["gender"]
        user.save()
        return redirect('home')
    return render(request, 'changeinfo.html')

def deleteaccount(request):

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('login')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'deleteaccount.html', {'password_form': password_form})

def search(request):
    blogs = None
    q = None
    if 'q' in request.GET:
        q = request.GET.get('q')
        blogs = UserProfile.objects.all().filter(Q(username__contains=q) | Q(gender__contains=q) | Q(birthdate__contains=q))
        return render(request, 'search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'search.html')


def post_detail(request, pk):
    post = UserProfile.objects.get(pk=pk)
    if post.role == 'S':
        submitter = get_object_or_404(Submitter,pk=pk)
        apply = ApplyTask.objects.filter(submitter=submitter)

        context = {
            'post': post, 'apply': apply, 'submitter': submitter
        }
        return render(request, 'post_detail.html', context)
    else:
        rater = get_object_or_404(Rater, pk=pk)
        parsed = ParsedData.objects.filter(rater=rater)

        context = {
            'post':post, 'pared': parsed
        }
        return render(request, 'post_detail.html', context)




