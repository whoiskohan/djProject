from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from .forms import *
from .models import *
from .utils import *


class WomanHome(DataMixin, ListView):
    model = Woman
    template_name = 'woman/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Home')
        context.update(context_def)
        return context

    def get_queryset(self):
        return Woman.objects.filter(is_published=True)


def about(request):
    content_list = Woman.objects.all()
    paginator = Paginator(content_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'woman/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'About website'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'woman/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Add page')
        context.update(context_def)
        return context


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


class ShowPost(DataMixin, DetailView):
    model = Woman
    template_name = 'woman/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context['post'])
        context.update(context_def)
        return context


class WomanCategory(DataMixin, ListView):
    model = Woman
    template_name = 'woman/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Woman.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Category: ' + str(context['posts'][0].category),
                                            category_selected=context['posts'][0].category_id)
        context.update(context_def)
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Page Not Found </h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'woman/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Register')
        context.update(context_def)
        return context


