from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jasleen Kaur',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 15, 2023'
    },
    {
        'author': 'Abhimanyu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 28, 2023'
    }
]

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About Page'})