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
    transactionId = models.CharField(max_length=9999999999999)
    atmCardNumber = models.CharField(max_length=9999999999999)
    date = models.DateField(max_length=50)
    ATMachineUID = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    responseCode = models.CharField(max_length=50)
    transactionType = models.CharField(max_length=50)


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


class PhoneChange(models.Model):
    newPhoneNumber = models.CharField(max_length=12)


class PinChange(models.Model):
    previousPin = models.CharField(max_length=4)
    newPin = models.CharField(max_length=4)


class CashWithdrawal(models.Model):
    amountTransferred = models.CharField(max_length=999999999999)
    denomination = models.CharField(max_length=50)
    currentBalance = models.CharField(max_length=9999999999999)


class CashTransfer(models.Model):
    beneficiaryAccountNumber = models.CharField(max_length=50)
    beneficiaryName = models.CharField(max_length=50)
    amountTransferred = models.CharField(max_length=999999999999)


class BalanceEnquiry(models.Model):
    balanceAmount = models.CharField(max_length=9999999999999)


class ATMachineRefill(models.Model):
    refillId = models.CharField(max_length=9999999999999)
    ATMachineUID = models.CharField(max_length=9999999999999)
    amount = models.CharField(max_length=9999999999999)
    atmBranch = models.CharField(max_length=9999999999999)
    refillDate = models.DateField(max_length=9999999999999)
    previousBalance = models.CharField(max_length=9999999999999)


class ATMachine(models.Model):
    ATMachineUID = models.CharField(max_length=9999999999999)
    currentBalance = models.CharField(max_length=9999999999999)
    location = models.CharField(max_length=9999999999999)
    minimumBalance = models.CharField(max_length=9999999999999)
    status = models.CharField(max_length=9999999999999)
    lastRefillDate = models.CharField(max_length=9999999999999)
    nextMaintenanceDate = models.CharField(max_length=9999999999999)


class AccountExtension(models.Model):
    accountNumber = models.CharField(max_length=9999999999999)
    name = models.CharField(max_length=9999999999999)
    phoneNumber = models.CharField(max_length=9999999999999)
    balance = models.CharField(max_length=9999999999999)
