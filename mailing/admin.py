
from django.contrib import admin
from mailing.models import Message, MailingSettings, MailingLogs


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Админка для сообщения рассылки
    """
    list_display = ('heading',)
    list_filter = ('heading',)
    search_fields = ('heading',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    """
    Админка для настроек рассылки
    """
    list_display = ('mailing_time', 'periodicity', 'status')
    list_filter = ('status',)


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    """
    Админка для логов
    """
    list_display = ('message', 'datatime_attempt', 'status', 'server_answer',)
    list_filter = ('message', 'status',)
