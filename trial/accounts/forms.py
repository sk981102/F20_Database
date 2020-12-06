from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField, PasswordChangeForm
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

class ChangeForm(forms.ModelForm):
    is_superuser = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    is_staff = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    class Meta:
        model = UserProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

class ChangeInfoForm(ChangeForm):
    is_superuser = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    is_staff = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    class Meta:
        model = UserProfile
        fields = ('user_id', 'first_name', 'last_name', 'username', 'birthdate', 'phone', 'address', 'gender','is_superuser','is_staff')
        exclude = ('is_superuser','is_staff')


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