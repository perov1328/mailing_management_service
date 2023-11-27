
from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """
    Модель клиента рассылки
    """
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    phone = models.CharField(max_length=25, **NULLABLE, verbose_name='Телефон')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    user = models.ManyToManyField(User, verbose_name='Пользователь')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f"{self.first_name} {self.last_name} (email: {self.email})"

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('first_name', 'last_name', 'registration_date',)
