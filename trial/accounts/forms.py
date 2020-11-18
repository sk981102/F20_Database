from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
#from django.utils import timezone

class SignUpForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user_id', 'first_name', 'last_name', 'username', 'PW','email','birthdate', 'phone', 'address', 'gender', 'role')

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'PW')
