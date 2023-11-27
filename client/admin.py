
from django.contrib import admin
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Админка для клиентов рассылки
    """
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('first_name', 'last_name',)
