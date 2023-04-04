from django.shortcuts import render
from blog.models import Post


def index(request):
    """Вьюха на домашней старницы."""
    posts = Post.objects.all()[:4]
    context = {
        'posts': posts
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')
