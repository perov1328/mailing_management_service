
from django import forms
from mailing.models import Message, MailingSettings
from client.forms import StyleFormMixin


class MessageForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для сообщения рассылки
    """
    class Meta:
        model = Message
        fields = '__all__'


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для настроек рассылки
    """
    class Meta:
        model = MailingSettings
        exclude = ('user', 'status',)
