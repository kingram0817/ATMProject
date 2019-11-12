from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('login.html', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('myAccount.html', views.myAccount, name="myAccount"),
    path('register.html', views.registerUser, name="register"),
    path('transactionHistory.html', views.transactionHistory, name="transactionHistory"),
    path('transferFunds.html', views.transferFunds, name="transferFunds"),
    path('withdrawFunds.html', views.withdrawFunds, name="withdrawFunds"),
    path('editAccount.html', views.editAccount, name="editAccount"),
]
