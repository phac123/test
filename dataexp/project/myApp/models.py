from django.db import models

# Create your models here.

class Users(models.Model):
    @classmethod
    def createUser(cls, account, password, name, age, gender, hobby, isD):
        user = cls(uaccount = account, upassword = password, uname = name, uage = age, ugender = gender,
                   uhobby = hobby, isDelete = isD)
        return user
    uaccount = models.CharField(max_length=20)
    upassword = models.CharField(max_length = 20)
    uname = models.CharField(max_length=20)
    uage = models.IntegerField(default=0)
    ugender = models.BooleanField(default=True)  #男：True
    uhobby = models.CharField(max_length=50)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "users"




