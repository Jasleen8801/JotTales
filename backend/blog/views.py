from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'Jasleen Kaur',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'July 15, 2023'
#     },
#     {
#         'author': 'Abhimanyu',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'May 28, 2023'
#     }
# ]


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')

    context = {
        # 'posts': posts
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, "blog/about.html", {"title": "About Page"})
