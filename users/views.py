from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import SignUpForm, editForm, CashTransferForm, CashWithdrawalForm, editPinNumber
from .models import Transaction, ATM_Card, CashTransfer, CashWithdrawal, ATMachine, CustomUser, AccountExtension


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged in!')
            return redirect('myAccount')
        else:
            messages.success(request, 'Error logging in - Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Thank you for registering')
            return redirect('myAccount')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def editAccount(request, userID):
    if request.method == 'POST':
        userData = CustomUser.objects.get(pk=userID)
        form = editForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Thank you for registering')
            return redirect('myAccount')
    else:
        form = editForm()
    context = {'form': form}
    return render(request, 'editAccount.html', context)


def home(request):
    return render(request, 'home.html', {})


def balanceEnquiry(request):
    return render(request, 'balanceEnquiry.html', {})


def about(request):
    all_locations = ATMachine.objects.all()
    return render(request, 'about.html', {'all_locations': all_locations})


def addCard(request):
    return render(request, 'addCard.html', {})


def myAccount(request):
    atmCard = ATM_Card.objects.get()
    # AccExt = AccountExtension.objects.get()
    # accountBalance = AccExt.balance
    return render(request, 'myAccount.html', {'atmCard': atmCard})


def transactionHistory(request):
    allTransactionHistory = Transaction.objects.all
    return render(request, 'transactionHistory.html', {'allTransactionHistory': allTransactionHistory})


def editPin(request):
    cardInfo = ATM_Card.objects.get()
    currentPin = cardInfo.pin

    if request.method == 'POST':
        form = editPinNumber(request.POST)
        if form.is_valid():
            messages.success(request, 'Edited Pin Successfully ')
            return redirect('myAccount.html')

    else:
        form = editPinNumber()

    return render(request, 'editPin.html', {'form': form})


def tFunds(request):
    allTransferItems = CashTransfer.objects.all()
    return render(request, 'transferFunds.html', {'allTransferItems': allTransferItems})


def wFunds(request):
    allWithdrawItems = CashWithdrawal.objects.all()
    return render(request, 'withdrawFunds.html', {'allWithdrawItems': allWithdrawItems})


def transferFunds(request):
    if request.method == 'POST':
        form = CashTransferForm(request.POST)
        if form.is_valid():
            return redirect('myAccount.html')
    else:
        form = CashTransferForm()

    return render(request, 'transferFunds.html', {'form': form})


def transferFunds(request):
    if request.method == 'POST':
        form = CashTransferForm(request.POST)
        if form.is_valid():
            return redirect('myAccount.html')
    else:
        form = CashTransferForm()

    return render(request, 'transferFunds.html', {'form': form})


def withdrawFunds(request):
    if request.method == 'POST':
        form = CashWithdrawalForm(request.POST)
        if form.is_valid():
            return redirect('myAccount.html')
    else:
        form = CashWithdrawalForm()

    return render(request, 'withdrawFunds.html', {'form': form})
