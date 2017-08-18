from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
# Create your views here.


def index(request):
    post_list = list(Post.objects.all())
    return render(request, 'mysite/index.html',
                  context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/detail.html',
                  context={'post': post})

