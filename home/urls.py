
from django.urls import path
from home.apps import HomeConfig
from home.views import *

app_name = HomeConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
