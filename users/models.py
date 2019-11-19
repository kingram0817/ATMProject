from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
import random


def getExpirationDate():
    return datetime.today() + timedelta(days=1460)


def setAccountNum():
    randomAccNum = random.randint(1, 99999999)
    return str(randomAccNum)


def CustomerAddressConcat():
    conCatAddress = str(CustomUser.address) + ' ' + str(CustomUser.city) + ', ' + str(CustomUser.state) + '. ' + str(
        CustomUser.zipCode)
    return conCatAddress


def CustomerNameConcat():
    conCatName = str(CustomUser.first_name) + ' ' + str(CustomUser.last_name)
    return conCatName


class CustomUser(AbstractUser):
    accountNumber = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zipCode = models.CharField(max_length=5, default='')
    phoneNumber = models.CharField(max_length=10, default='')

    def __str__(self):
        return str(self.accountNumber) + ' ' + str(self.last_name) + ' ' + str(self.first_name)


class Transaction(models.Model):
    DENIED = 'DE'
    SUCCESSFUL = 'SU'
    TRANSFER = 'TR'
    WITHDRAW = 'WD'

    STATUS_CHOICES = [
        (DENIED, 'Denied'),
        (SUCCESSFUL, 'Successful'),

    ]
    TRANSACTION_CHOICES = [

        (TRANSFER, 'Transfer'),
        (WITHDRAW, 'Withdraw'),
    ]

    transactionId = models.AutoField(primary_key=True)
    ATMCardNumber = models.ForeignKey('ATM_Card', db_column='ATMCardNumber', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today)
    ATMachineUID = models.ForeignKey('ATMachine', db_column='ATMachineUID', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DENIED)
    responseCode = models.CharField(max_length=50, default='')
    transactionType = models.CharField(max_length=2, choices=TRANSACTION_CHOICES, default=TRANSFER)


class ATM_Card(models.Model):
    DEACTIVATED = 'DE'
    ACTIVE = 'AC'

    CARD_STATUS = [(DEACTIVATED, 'Deactivated'), (ACTIVE, 'Active')]

    atmCardNumber = models.CharField(max_length=10, primary_key=True)
    accountNumber = models.ForeignKey('CustomUser', db_column='accountNumber', on_delete=models.CASCADE)
    pin = models.CharField(max_length=4, default='0000')
    name = models.CharField(max_length=100, default=CustomerNameConcat())
    # TODO:Change to DateField
    creationDate = models.DateField(default=datetime.today)
    # TODO:Change to DateField
    expirationDate = models.DateField(default=getExpirationDate)
    address = models.CharField(max_length=100, default=CustomerAddressConcat())
    phoneNumber = models.CharField(max_length=10, default=CustomUser.phoneNumber)
    cardStatus = models.CharField(max_length=2, choices=CARD_STATUS, default=DEACTIVATED)
    twoFactorAuthenticationStatus = models.BooleanField(default=True)
    currentBalance = models.IntegerField(default=500)

    def __str__(self):
        return str(self.atmCardNumber)


class PhoneChange(models.Model):
    newPhoneNumber = models.CharField(max_length=10, default='')


class PinChange(models.Model):
    previousPin = models.CharField(max_length=4, default=ATM_Card.pin)
    newPin = models.CharField(max_length=4, default='')


class CashWithdrawal(models.Model):
    USD = 'US'
    CAN = 'CA'

    DENOM_CHOICES = [
        (USD, 'USD'),
        (CAN, 'CAN'),

    ]
    amountTransferred = models.PositiveIntegerField(default=0)
    denomination = models.CharField(max_length=2, choices=DENOM_CHOICES, default=USD)
    currentBalance = models.IntegerField(default=ATM_Card.currentBalance)


class CashTransfer(models.Model):
    beneficiaryAccountNumber = models.CharField(max_length=50, default='')
    beneficiaryName = models.CharField(max_length=50, default='')
    amountTransferred = models.PositiveIntegerField(default=0)


class BalanceEnquiry(models.Model):
    balanceAmount = models.IntegerField(default=ATM_Card.currentBalance)


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

    def __str__(self):
        return str(self.ATMachineUID)


class AccountExtension(models.Model):
    accountNumber = models.ForeignKey('CustomUser', db_column='accountNumber', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=CustomerNameConcat)
    phoneNumber = models.CharField(max_length=10, default=CustomUser.phoneNumber)
    balance = models.IntegerField(default=ATM_Card.currentBalance)
