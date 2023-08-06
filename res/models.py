from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    ordernum=models.CharField(max_length=12)
    msg=models.TextField(max_length=100)

class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)

class Register(models.Model):
    gen=(
        ('Male','Male'),
        ('Female', 'Female')

    )
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=15)
    phone=models.IntegerField()
    regusername=models.CharField(max_length=15)
    regpassword=models.CharField(max_length=15)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

