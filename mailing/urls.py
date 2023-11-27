
from django.urls import path
from django.views.decorators.cache import cache_page
from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    path('messages/', cache_page(60)(MessageListView.as_view()), name='messages'),
    path('create/message/', MessageCreateView.as_view(), name='create_message'),
    path('update/message/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('detail/message/<int:pk>', cache_page(60)(MessageDetailView.as_view()), name='message_detail'),
    path('delete/message/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('settings/', MailingSettingsListView.as_view(), name='settings'),
    path('create/settings/', MailingSettingsCreateView.as_view(), name='create_settings'),
    path('update/settings/<int:pk>', MailingSettingsUpdateView.as_view(), name='settings_update'),
    path('detail/settings/<int:pk>', MailingSettingsDetailView.as_view(), name='settings_detail'),
    path('delete/settings/<int:pk>', MailingSettingsDeleteView.as_view(), name='settings_delete'),
    path('logs/', cache_page(60)(MailingLogsListView.as_view()), name='logs'),
]
