from django.shortcuts import render
from django.utils import timezone
from posts.models import Post


# Create your views here.

def index(request):
    latest_post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    posts = ["posts/"]*4 
    for post_idx in range(latest_post_list.count()):
        posts[post_idx] = "posts/" + latest_post_list[post_idx].slug
    return render(request, 'homepage/index.html', {'post_1':posts[0], 'post_2':posts[1], 'post_3':posts[2], 'post_4':posts[3]})

def about(request):
    return render(request, 'homepage/about.html')

def register(request):
    return render(request, 'homepage/register.html')

