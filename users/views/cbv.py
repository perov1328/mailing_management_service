import secrets
from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView
from users.forms import RegisterForm, ProfileForm
from users.models import User


class LoginView(BaseLoginView):
    """
    Контроллер входа в учетную запись
    """
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    """
    Контроллер выхода из учетной записи
    """
    pass


class RegisterView(CreateView):
    """
    Контроллер для регистрации пользователя на платформе
    """
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.verification_key = secrets.randbelow(1_000_000)
        new_user.save()

        token = urlsafe_base64_encode(force_bytes(new_user.verification_key))
        verification_url = reverse('users:verify', kwargs={'token': token})
        send_mail(
            subject='Заверешение регистрации на Mail Manager by 13|28',
            message=f'Для подтвердения регистрации, пройдите по ссылке ниже: \n {self.request.build_absolute_uri(verification_url)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    """
    Контролер для работы с профилем пользователя
    """
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
