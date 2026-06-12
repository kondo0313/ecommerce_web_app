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


class UserSignupForm(forms.Form):
    user_id = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    password_confirm = forms.CharField(max_length=20, required=False)
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # 両方入力されてるときだけチェック
        if password and password_confirm:
            if password != password_confirm:
                self.add_error("password_confirm", "パスワードが一致しません")

        return cleaned_data
