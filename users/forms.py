
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from client.forms import StyleFormMixin
from users.models import User


class RegisterForm(StyleFormMixin, UserCreationForm):
    """
    Форма для регистрации пользователя платформы
    """
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileForm(StyleFormMixin, UserChangeForm):
    """
    Форма для работы с профилем пользователя платформы
    """
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()