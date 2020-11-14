from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from rater.models import Rater
from my_admin.models import MyAdmin
from submitter.models import Submitter
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils import timezone


class UserProfile(AbstractUser):
    """
    계정 Attributes
    user_id : PK (Auto_increment ID, (int))
    username : Char
    PW : Char
    Gender : M/F
    Birthdate : Date
    Address : Char
    Phone Number : Int or Char
    Role : Admin/Submitter/Rater
    """
    GENDER = (('M', 'Male'), ('F', 'Female'))
    ROLE = (('A', 'Admin'), ('R', 'Rater'), ('S', 'Submitter'))

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, default='na')
    last_name = models.CharField(max_length=30, default='na')
    username = models.CharField(max_length=10,unique=True)
    PW = models.CharField(max_length=12, default="na")
    email = models.EmailField(max_length=254, default='na')
    birthdate = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=11, default="01012343434")
    address = models.CharField(max_length=100, default="na")
    gender = models.CharField(max_length=6, choices=GENDER, default="na")
    role = models.CharField(max_length=10, choices=ROLE, default="na")

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'PW'
    REQUIRED_FIELDS = ['first_name','last_name']

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created and self.role == 'A':
            MyAdmin.objects.create(user_id=self)
        if created and self.role == 'R':
            Rater.objects.create(user_id=self)
        if created and self.role == 'S':
            Submitter.objects.create(user_id=self)


class UserManager(BaseUserManager):
    def _create_user(self,first_name, last_name, username, PW,email, birthdate, phone, address, gender, role, **extrafields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        print(self)
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            PW = PW,
            email =email,
            birthdate = birthdate,
            phone = phone,
            address = address,
            gender = gender,
            role = role, **extrafields
        )
        user.set_password(PW)
        user.save(using=self._db)
        return user

    def create_user(self, username, PW,email,role,**extra_fields):
        print(self)
        if role == 'A':
            self.create_superuser(self,username, PW,email, **extra_fields)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email,username, PW, **extra_fields)

    def create_superuser(self, username, PW, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(username, PW, email,**extra_fields)

