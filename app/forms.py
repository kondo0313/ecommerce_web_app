from django import forms
from .models import AccountUser

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AccountUser
        fields = ["user_id", "password", "name", "address"]


class UserLoginForm(forms.Form):
    user_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
