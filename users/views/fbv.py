
from random import randint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from users.models import User


@login_required
def generate_new_password(request):
    """
    Контроллер для генерации нового пароля для пользователя и отправка его на почту
    """
    new_password = ''.join([str(randint(0, 9)) for _ in range(10)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('client:clients'))


def verify_email(request, token):
    try:
        user_verification_key = urlsafe_base64_decode(token).decode()
        user = User.objects.get(verification_key=user_verification_key)
        if int(user_verification_key) == int(user.verification_key):
            user.is_active = True
            user.save()
            messages.success(request, 'Ваш аккаунт был успешно подтвержден. Теперь вы можете войти.')
            return redirect('home:home')
        else:
            messages.error(request, 'Ошибка верификации аккаунта.')
            return HttpResponse("Ошибка верификации аккаунта.")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Ошибка верификации аккаунта.')
        return HttpResponse("Ошибка верификации аккаунта.")