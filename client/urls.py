
from django.urls import path
from django.views.decorators.cache import cache_page
from client.apps import ClientConfig
from client.views import *

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('create/client/', cache_page(60)(ClientCreateView.as_view()), name='create_client'),
    path('update/client/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('detail/client/<int:pk>', cache_page(60)(ClientDetailView.as_view()), name='client_detail'),
    path('delete/client/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
