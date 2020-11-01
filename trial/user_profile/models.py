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
    user_id = models.AutoField(primary_key=True)
