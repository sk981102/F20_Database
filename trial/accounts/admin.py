from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import SignUpForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    model = UserProfile

admin.site.register(UserProfile, CustomUserAdmin)
