from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть логін'
        })
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть пароль'
        })
    )

    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторіть пароль'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']