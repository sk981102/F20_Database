from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
#from django.utils import timezone
from django.contrib.auth.hashers import check_password

class SignUpForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user_id', 'first_name', 'last_name', 'username', 'PW','email','birthdate', 'phone', 'address', 'gender', 'role')

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'PW')

class ViewUsers(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'PW','email','birthdate', 'phone', 'address', 'gender', 'role')

class ChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'birthdate', 'phone', 'address', 'gender')


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='PW', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')