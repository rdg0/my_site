from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from . models import Category, Comment, Post


def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/all_posts.html', context)


def by_category(request, slug):

    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/by_category.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
        return redirect('blog:post_detail', post_id=post_id)
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)
