from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.utils import timezone


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'PW','email','birthdate', 'phone', 'address', 'gender', 'role')
