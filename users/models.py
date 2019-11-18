from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta


def getExpirationDate():
    return datetime.today() + timedelta(days=1460)


class CustomUser(AbstractUser):
    accountNumber = models.CharField(max_length=10, primary_key=True, default='34')
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zipCode = models.CharField(max_length=5, default='')
    phoneNumber = models.CharField(max_length=10, default='1112223333')

    def __str__(self):
        return str(self.accountNumber)


class Transaction(models.Model):
    DENIED = 'DE'
    SUCCESSFUL = 'SU'

    STATUS_CHOICES = [
        (DENIED, 'Denied'),
        (SUCCESSFUL, 'Successful'),

    ]

    transactionId = models.AutoField(primary_key=True)
    ATMCardNumber = models.ForeignKey('ATM_Card', db_column='ATMCardNumber', on_delete=models.CASCADE)
    date = models.DateField(max_length=50, default='')
    ATMachineUID = models.ForeignKey('ATMachine', db_column='ATMachineUID',on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DENIED)
    responseCode = models.CharField(max_length=50, default='')
    transactionType = models.CharField(max_length=50, default='')


def CustomerAddressConcat():
    conCatAddress = str(CustomUser.address) + ' ' + str(CustomUser.city) + ', ' + str(CustomUser.state) + '. ' + str(CustomUser.zipCode)
    return conCatAddress


def CustomerNameConcat():
    conCatName = str(CustomUser.first_name) + ' ' + str(CustomUser.last_name)
    return conCatName


class ATM_Card(models.Model):
    atmCardNumber = models.CharField(max_length=10, primary_key=True)
    accountNumber = models.ForeignKey('CustomUser', db_column='accountNumber', on_delete=models.CASCADE)
    pin = models.CharField(max_length=4, default='0000')
    name = models.CharField(max_length=100, default='')
    # TODO:Change to DateField
    creationDate = models.DateField(default=datetime.today)
    # TODO:Change to DateField
    expirationDate = models.DateField(default=getExpirationDate)
    address = models.CharField(max_length=100, default='')
    phoneNumber = models.CharField(max_length=10, default='')
    cardStatus = models.BooleanField(default=True)
    twoFactorAuthenticationStatus = models.BooleanField(default=True)


class PhoneChange(models.Model):
    newPhoneNumber = models.CharField(max_length=10, default='1112223333')


class PinChange(models.Model):
    previousPin = models.CharField(max_length=4, default='')
    newPin = models.CharField(max_length=4, default='')


class CashWithdrawal(models.Model):
    amountTransferred = models.PositiveIntegerField(default=0)
    denomination = models.CharField(max_length=3, default='USD')
    currentBalance = models.IntegerField(default=0)


class CashTransfer(models.Model):
    beneficiaryAccountNumber = models.CharField(max_length=50, default='')
    beneficiaryName = models.CharField(max_length=50, default='')
    amountTransferred = models.PositiveIntegerField(default=0)


class BalanceEnquiry(models.Model):
    balanceAmount = models.IntegerField(default=0)


class ATMachineRefill(models.Model):
    refillId = models.AutoField(primary_key=True)
    ATMachineUID = models.ForeignKey('ATMachine', db_column='ATMachineUID', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    atmBranch = models.CharField(max_length=50, default='')
    refillDate = models.DateField(max_length=50, default='')
    previousBalance = models.PositiveIntegerField(default=0)


class ATMachine(models.Model):
    ATMachineUID = models.AutoField(primary_key=True)
    currentBalance = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, default='')
    minimumBalance = models.PositiveIntegerField(default=1000)
    status = models.CharField(max_length=50, default='')
    lastRefillDate = models.DateField(max_length=50, default='')
    # TODO:Test nextMaintenanceDate
    nextMaintenanceDate = models.DateField(max_length=50, default='')


class AccountExtension(models.Model):
    accountNumber = models.ForeignKey('CustomUser', db_column='accountNumber', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=10, default='1112223333')
    balance = models.IntegerField(default=0)
