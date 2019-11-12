from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm, editForm
from .models import CustomUser, Transaction


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = editForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser)
