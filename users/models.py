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
    transactionId = models.CharField(max_length=9999999999999, default='')
    atmCardNumber = models.CharField(max_length=9999999999999, default='')
    date = models.DateField(max_length=50, default='')
    ATMachineUID = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')
    responseCode = models.CharField(max_length=50, default='')
    transactionType = models.CharField(max_length=50, default='')


class ATM_Card(models.Model):
    atmCardNumber = models.CharField(max_length=50, default='')
    accountNumber = models.CharField(max_length=50, default='')
    pin = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    dateOfIssue = models.CharField(max_length=50, default='')
    expirationDate = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=50, default='')
    cardStatus = models.CharField(max_length=50, default='')
    twoFactorAuthenticationStatus = models.BooleanField(default=True)


class PhoneChange(models.Model):
    newPhoneNumber = models.CharField(max_length=12, default='')


class PinChange(models.Model):
    previousPin = models.CharField(max_length=4, default='')
    newPin = models.CharField(max_length=4, default='')


class CashWithdrawal(models.Model):
    amountTransferred = models.CharField(max_length=999999999999, default='')
    denomination = models.CharField(max_length=50, default='')
    currentBalance = models.CharField(max_length=9999999999999, default='')


class CashTransfer(models.Model):
    beneficiaryAccountNumber = models.CharField(max_length=50, default='')
    beneficiaryName = models.CharField(max_length=50, default='')
    amountTransferred = models.CharField(max_length=999999999999, default='')


class BalanceEnquiry(models.Model):
    balanceAmount = models.CharField(max_length=9999999999999, default='')


class ATMachineRefill(models.Model):
    refillId = models.CharField(max_length=9999999999999, default='')
    ATMachineUID = models.CharField(max_length=9999999999999, default='')
    amount = models.CharField(max_length=9999999999999, default='')
    atmBranch = models.CharField(max_length=9999999999999, default='')
    refillDate = models.DateField(max_length=9999999999999, default='')
    previousBalance = models.CharField(max_length=9999999999999, default='')


class ATMachine(models.Model):
    ATMachineUID = models.CharField(max_length=9999999999999, default='')
    currentBalance = models.CharField(max_length=9999999999999, default='')
    location = models.CharField(max_length=9999999999999, default='')
    minimumBalance = models.CharField(max_length=9999999999999, default='')
    status = models.CharField(max_length=9999999999999, default='')
    lastRefillDate = models.CharField(max_length=9999999999999, default='')
    nextMaintenanceDate = models.CharField(max_length=9999999999999, default='')


class AccountExtension(models.Model):
    accountNumber = models.CharField(max_length=9999999999999, default='')
    name = models.CharField(max_length=9999999999999, default='')
    phoneNumber = models.CharField(max_length=9999999999999, default='')
    balance = models.CharField(max_length=9999999999999, default='')
