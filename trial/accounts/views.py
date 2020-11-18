from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
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
            """
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('PW')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
            """
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
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def viewusers(request):
    form = UserProfile.objects.all()
    #content = {'viewusers' : form}
    return render(request, 'viewusers.html', {'form': form})