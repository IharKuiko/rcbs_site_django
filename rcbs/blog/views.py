from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'RCBS'
        return context


def get_category(request, slug):
    return render(request, 'blog/index.html')

def get_post(request, slug):
    return render(request, 'blog/index.html')