from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm, editForm
from .models import CustomUser, Transaction, ATM_Card, PhoneChange, PinChange, CashWithdrawal, CashTransfer, BalanceEnquiry, ATMachine, ATMachineRefill, AccountExtension


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = editForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser)
admin.site.register(Transaction)
admin.site.register(ATM_Card)
admin.site.register(PhoneChange)
admin.site.register(PinChange)
admin.site.register(CashWithdrawal)
admin.site.register(CashTransfer)
admin.site.register(BalanceEnquiry)
admin.site.register(ATMachine)
admin.site.register(ATMachineRefill)
admin.site.register(AccountExtension)
