from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Dhvanesh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 13 2020',
    },
    {
        'author': 'Hetal',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Sep 12 2020',
    }
]
# Create your views here.


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
