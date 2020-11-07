from django.db import models
from rater.models import Rater
from my_admin.models import MyAdmin
from submitter.models import Submitter

# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    """
    계정 Attributes
    user_id : PK (Auto_increment ID, (int))
    ID : Char
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
    ID = models.CharField(max_length=10, default="na")
    PW = models.CharField(max_length=12, default="na")
    birthdate = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=11, default="01012343434")
    address = models.CharField(max_length=100, default="na")
    gender = models.CharField(max_length=6, choices=GENDER,default="na")
    role = models.CharField(max_length=10, choices=ROLE,default="na")

    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created and self.role=='A':
            MyAdmin.objects.create(user_id=self)
        if created and self.role=='R':
            Rater.objects.create(user_id=self)
        if created and self.role=='S':
            Submitter.objects.create(user_id=self)
    



