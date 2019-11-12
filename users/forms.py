from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Transaction, ATM_Card
import random


def setTransactions():
    Transaction.amount = '$1000'


def setAccountNumber():
    ATM_Card.accountNumber = random.randint(1, 9999999999)
    CustomUser.accountNumber = ATM_Card.accountNumber


class SignUpForm(UserCreationForm):
    accountNumber = forms.CharField(max_length=16)
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
    setAccountNumber()

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
    pass

# class CashTransferForm(models.Model):
# beneficiaryAccountNumber = forms.CharField(max_length=50)
# beneficiaryName = forms.CharField(max_length=50)
# amountTransferred = forms.CharField(max_length=999999999999)
