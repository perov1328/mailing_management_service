
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from client.forms import ClientForm
from client.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(LoginRequiredMixin, ListView):
    """
    Контроллер для вывода всех клиентов рассылки
    """
    model = Client
    login_url = 'users:login'


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания клиента рассылки
    """
    model = Client
    form_class = ClientForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')

    def get_context_data(self, **kwargs):
        """
        Метод получения контекста
        """
        context_data = super().get_context_data()
        user = self.request.user
        context_data['user'] = user
        return context_data

    def form_valid(self, form):
        """
        Метод получения данных из формы
        """
        if form.is_valid():
            user = self.request.user
            new_user = form.save()
            new_user.user.add(user)
            new_user.save()
            return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления данных о клиенте рассылки
    """
    model = Client
    form_class = ClientForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления клиента рассылки
    """
    model = Client
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра данных клиента
    """
    model = Client
    login_url = 'users:login'
