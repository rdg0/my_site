from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>', views.by_category, name='by_category'),
    path('', views.all_posts, name='all_posts'),
    
]