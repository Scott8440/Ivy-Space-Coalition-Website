from django.shortcuts import render
from django.utils import timezone

from .models import Post

def index(request):
    latest_post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'posts/index.html', 
              {'latest_post_list':latest_post_list})

def detail(request, post_slug):
    post = (Post.objects.filter(slug=post_slug)[0])
    return render(request, 'posts/detail.html', {'post_slug': post_slug, 'post':post})

def category(request, category_slug):
    category_posts = (Post.objects.filter(category__slug=category_slug)
                        .filter(pub_date__lte=timezone.now())
                        .order_by('-pub_date'))
    return render(request, 'posts/category.html', {'latest_post_list': category_posts})
