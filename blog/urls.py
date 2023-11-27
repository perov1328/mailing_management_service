
from django.urls import path
from django.views.decorators.cache import cache_page
from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', cache_page(60)(BlogListView.as_view()), name='blogs'),
    path('create/blog/', BlogCreateView.as_view(), name='create_blog'),
    path('update/blog/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('detail/blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('delete/blog/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
