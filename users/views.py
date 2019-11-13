from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import SignUpForm, editForm, CashTransferForm, CashWithdrawalForm
from .models import Transaction, ATM_Card, CashTransfer, CashWithdrawal, ATMachine


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


def editAccount(request):
    if request.method == 'POST':
        form = editForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully edited your account. ')
            return redirect('myAccount')
    else:
        form = editForm()
    context = {'form': form}
    return render(request, 'editAccount.html', context)


def home(request):
    return render(request, 'home.html', {})


def about(request):
    all_locations = ATMachine.location
    return render(request, 'about.html', {'all_locations': all_locations})


def myAccount(request):
    accountN = ATM_Card.accountNumber
    return render(request, 'myAccount.html', {'accountN': accountN})


def transactionHistory(request):
    allTransactionHistory = Transaction.objects.all
    return render(request, 'transactionHistory.html', {'allTransactionHistory': allTransactionHistory})


def transferFunds1(request):
    beneAccNumber = CashTransfer.beneficiaryAccountNumber
    beneName = CashTransfer.beneficiaryName
    amountTrans = CashTransfer.amountTransferred
    return render(request, 'transferFunds.html',
                  {'beneAccNumber': beneAccNumber, 'beneName': beneName, 'amountTrans': amountTrans})


def withdrawFunds1(request):
    cashWithdrawalAmount = CashWithdrawal.amountTransferred
    cashWithdrawalDenom = CashWithdrawal.denomination
    cashWithdrawalBalance = CashWithdrawal.currentBalance
    return render(request, 'withdrawFunds.html',
                  {'cashWithdrawalAmount': cashWithdrawalAmount, 'cashWithdrawalDenom': cashWithdrawalDenom,
                   'cashWithdrawalBalance': cashWithdrawalBalance})


def transferFunds(request):
    if request.method == 'POST':
        form = CashTransferForm(request.POST)
        if form.is_valid():
            beneAccNumber = CashTransfer.beneficiaryAccountNumber
            beneName = CashTransfer.beneficiaryName
            amountTrans = CashTransfer.amountTransferred
            return render(request, 'transferFunds.html',
                          {'beneAccNumber': beneAccNumber, 'beneName': beneName, 'amountTrans': amountTrans})
    else:
        form = CashTransferForm()

    return render(request, 'transferFunds.html', {'form': form})


def withdrawFunds(request):
    if request.method == 'POST':
        form = CashWithdrawalForm(request.POST)
        if form.is_valid():
            cashWithdrawalAmount = CashWithdrawal.amountTransferred
            cashWithdrawalDenom = CashWithdrawal.denomination
            cashWithdrawalBalance = CashWithdrawal.currentBalance
            return render(request, 'withdrawFunds.html',
                          {'cashWithdrawalAmount': cashWithdrawalAmount, 'cashWithdrawalDenom': cashWithdrawalDenom,
                           'cashWithdrawalBalance': cashWithdrawalBalance})
    else:
        form = CashWithdrawalForm()

    return render(request, 'withdrawFunds.html', {'form': form})
