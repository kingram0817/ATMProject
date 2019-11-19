from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Transaction, ATM_Card
import random


def setAccountNum():
    ATM_Card.accountNumber = random.randint(1, 999999)
    CustomUser.accountNumber = ATM_Card.accountNumber


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    first_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    address = forms.CharField(max_length=50, label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}))
    city = forms.CharField(max_length=50, label="",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}))
    state = forms.CharField(max_length=2, label="",
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}))
    zipCode = forms.CharField(max_length=5, label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Zip'}))
    phoneNumber = forms.CharField(max_length=10, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))

    # setAccountNum()

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'city', 'state',
                  'zipCode', 'phoneNumber',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields[
            'username'].help_text = '<div class="form-text text-muted"><small>Required. 150 characters or fewer.' \
                                    ' Letters, digits and @/./+/-/_ only</small></div>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class= "form-text text-muted small">' \
                                             '<li>Your password can\'t be too similar to your other personal information.</li>' \
                                             '<li>Your password must contain at least 8 characters.</li>' \
                                             '<li>Your password can\'t be a commonly used password.</li>' \
                                             '<li>Your password can\'t be entirely numeric.</li>' \
                                             '</ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields[
            'password2'].help_text = '<div class="form-text text-muted"><small>Enter the same password as before, for verification.</small></div>'


class editForm(UserChangeForm):
    password = None
    username = forms.CharField(max_length=50, label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    first_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    address = forms.CharField(max_length=50, label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}))
    city = forms.CharField(max_length=50, label="",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}))
    state = forms.CharField(max_length=2, label="",
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}))
    zipCode = forms.CharField(max_length=5, label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Zip'}))
    phoneNumber = forms.CharField(max_length=10, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    ATM_Card.pin = forms.CharField(max_length=4, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter New Pin'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'state',
                  'zipCode', 'phoneNumber',)

    def __init__(self, *args, **kwargs):
        super(editForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields[
            'username'].help_text = '<div class="form-text text-muted"><small>Required. 150 characters or fewer.' \
                                    ' Letters, digits and @/./+/-/_ only</small></div>'


class editPinNumber(forms.Form):
    ATM_Card.pin = forms.CharField(label='', max_length=4, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter New Pin Number', 'style': 'margin-bottom:15px;'}))


class CashTransferForm(forms.Form):
    beneficiaryAccountNumber = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Account Number', 'style': 'margin-bottom:15px;'}))
    beneficiaryName = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'margin-bottom:15px;'}))
    amountTransferred = forms.CharField(label='', max_length=999999999999, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Transfer Amount', 'style': 'margin-bottom:15px;'}))


class CashWithdrawalForm(forms.Form):
    amountTransferred = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Transfer Amount', 'style': 'margin-bottom:15px;'}))
    denomination = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Denomination', 'style': 'margin-bottom:15px;'}))
    currentBalance = forms.CharField(label='', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Current Balance', 'style': 'margin-bottom:15px;'}))

# class AddNewCard(forms.Form):
#    amountTransferred = forms.CharField(label='', max_length=50, widget=forms.TextInput(
#        attrs={'class': 'form-control', 'placeholder': 'Transfer Amount', 'style': 'margin-bottom:15px;'}))
#    denomination = forms.CharField(label='', max_length=50, widget=forms.TextInput(
#        attrs={'class': 'form-control', 'placeholder': 'Denomination', 'style': 'margin-bottom:15px;'}))
#    currentBalance = forms.CharField(label='', max_length=50, widget=forms.TextInput(
#        attrs={'class': 'form-control', 'placeholder': 'Current Balance', 'style': 'margin-bottom:15px;'}))
