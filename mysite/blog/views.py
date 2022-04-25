from django.shortcuts import render
from . models import Post
from django.utils import timezone

# Create your views here.

def post_list(requst):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(requst, 'blog/post_list.html',{'our_posts':posts})