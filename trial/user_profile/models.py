from django.db import models


# Create your models here.
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
    ID = models.CharField(max_length=10)
    PW = models.CharField(max_length=12)
    birthdate = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER)
    role = models.CharField(max_length=10, choices=ROLE)
    
    
