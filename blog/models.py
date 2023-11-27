
from django.db import models
from client.models import NULLABLE


class Blog(models.Model):
    """
    Модель блога
    """
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    date_of_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'Блог: {self.title}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title', 'date_of_published',)
