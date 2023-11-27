
from django.db import models
from client.models import Client
from users.models import User


PERIODICITY_CHOICES = [
    ('Daily', 'Раз в день'),
    ('Weekly', 'Раз в неделю'),
    ('Monthly', 'Раз в месяц'),
]


STATUS_CHOICES = [
    ('Started', 'В процессе'),
    ('Completed', 'Завершена'),
]


class Message(models.Model):
    """
    Модель для сообщения рассылки
    """
    heading = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(verbose_name='Текст')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'Рассылка на тему: "{self.heading}".'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    """
    Модель для настроек рассылки
    """
    name = models.CharField(max_length=100, verbose_name='Наименование рассылки')
    mailing_time = models.TimeField(verbose_name='Время рассылки')
    mailing_date = models.DateField(verbose_name='Дата рассылки')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Started', verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.mailing_time} - {self.periodicity}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class MailingLogs(models.Model):
    """
    Модель логов отправки рассылок
    """
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, verbose_name='Сообщение')
    datatime_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=30, verbose_name='Статус попытки')
    server_answer = models.TextField(verbose_name='Ответ почтового сервера')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.message} - {self.status}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
