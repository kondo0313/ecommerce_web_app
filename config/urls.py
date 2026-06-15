"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import (
    index,
    admin_register,
    user_register,
    user_register_commit,
    user_login,
    user_info,
    user_update,
    user_update_commit,
    withdraw_confirm,
    withdraw_commit,
    serch_result,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('SerchResult/', serch_result, name='serch_result'),
    path('accounts/AdminRegister/', admin_register, name='admin_register'),
    path('accounts/UserRegister/', user_register, name='user_register'),
    path('accounts/RegisterUserCommit/', user_register_commit, name='user_register_commit'),
    path('accounts/UserLogin/', user_login, name='user_login'),
    path('accounts/UserInfo/', user_info, name='user_info'),
    path('accounts/UserUpdate/', user_update, name='user_update'),
    path("accounts/UpdateUserCommit/", user_update_commit, name="user_update_commit"),
    path("accounts/WithdrawConfirm/", withdraw_confirm, name="withdraw_confirm"),
    path("accounts/WithdrawCommit/", withdraw_commit, name="withdraw_commit"),
]