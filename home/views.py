
import random
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from blog.models import Blog
from client.models import Client
from mailing.models import MailingSettings


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Контроллер для вывода домашней страницы
    """
    login_url = 'users:login'
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        """
        Метод для получения контекста домашней страницы
        """
        user = self.request.user
        if self.request.method == 'GET':
            if settings.CACHE_ENABLED:
                key = 'cached_statistics'
                cached_context = cache.get(key)
                if cached_context is None:
                    context = super().get_context_data(*args, **kwargs)
                    if not user.is_staff:
                        context['total_mailing'] = MailingSettings.objects.filter(user=user).count()
                        context['active_mailing'] = MailingSettings.objects.filter(user=user).filter(status='enabled').count()
                        context['clients_count'] = Client.objects.filter(user=user).distinct('email').count()
                    else:
                        context['total_mailing'] = MailingSettings.objects.all().count()
                        context['active_mailing'] = MailingSettings.objects.all().filter(status='Started').count()
                        context['clients_count'] = Client.objects.all().count()
                        main_page_context = {
                            'total_mailing': context['total_mailing'],
                            'active_mailing': context['active_mailing'],
                            'clients_count': context['clients_count']
                        }
                        cache.set(key, main_page_context)
                        all_blog_articles = Blog.objects.all()
                        random_articles = random.sample(list(all_blog_articles), 3)
                        context['random_articles'] = random_articles
                    return context
                else:
                    context = super().get_context_data(*args, **kwargs)
                    context['total_mailing'] = cached_context['total_mailing']
                    context['active_mailing'] = cached_context['active_mailing']
                    context['clients_count'] = cached_context['clients_count']
                    all_blog_articles = Blog.objects.all()
                    random_articles = random.sample(list(all_blog_articles), 3)
                    context['random_articles'] = random_articles
                return context
