
from django.core.mail import send_mail
from datetime import datetime, timedelta
from mailing.models import MailingLogs, MailingSettings, Message
from config import settings


def my_scheduled_job():
    """
    Функция для отправки сообщений, согласно заданным настройкам
    """
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    messages = MailingSettings.objects.all()

    for el in messages:
        clients = el.clients.values_list('email', flat=True)
        if el.mailing_time <= current_time and el.mailing_date == current_date and el.status == 'Started':
            try:
                send_mail(
                    subject=el.message.heading,
                    message=el.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=clients  # передача списка email в качестве получателей
                )

                if el.periodicity == 'Daily':
                    el.mailing_date += timedelta(days=1)
                elif el.periodicity == 'Weekly':
                    el.mailing_date += timedelta(days=7)
                elif el.periodicity == 'Monthly':
                    el.mailing_date += timedelta(days=30)
                el.save()
                MailingLogs.objects.create(message=el.message, status='Ok', server_answer='Complete')

            except Exception:
                MailingLogs.objects.create(message=el.message, status='tired :(',
                                           server_answer="Sorry, I'm broken")
