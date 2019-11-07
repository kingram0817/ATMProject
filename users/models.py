from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    accountNumber = models.CharField(max_length=16, default='8888000011112222')
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zipCode = models.CharField(max_length=5, default='12345')
    phoneNumber = models.CharField(max_length=10, default='123456789')

    def __str__(self):
        return self.accountNumber


class Transaction(models.Model):
    action = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    amount = models.CharField(max_length=50)
    account = models.CharField(max_length=50)


class ATM_Card(models.Model):

    atmCardNumber = models.CharField(max_length=50, default='')
    accountNumber = models.CharField(max_length=50, default='')
    pin = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    #dateOfIssue
    #expirationDate
    #address
    #twoFactorAuthenticationStatus
    #phoneNumber
    #cardStatus