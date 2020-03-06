
from django.db import models
from datetime import timedelta
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.

class User(AbstractBaseUser):
    STATUS_CHOICES = (
        ('1', 'A+'),
        ('2', 'A-'),
        ('3', 'B+'),
        ('4', 'B-'),
        ('5', 'AB+'),
        ('6', 'AB-'),
        ('7', 'O+'),
        ('8', 'O-')
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    nationalCode = models.CharField(max_length=15)
    insuranceCode = models.CharField(max_length=30)
    addressImage = models.ImageField(upload_to='img/profile/')
    credit = models.IntegerField()
    addressHome = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=15)
    about = models.TextField()
    status = models.CharField("گروه خونی", max_length=10, choices=STATUS_CHOICES, default='draft')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'


class VipRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    startDate = models.DateField(auto_now=True)
    endDate = models.DateField()
