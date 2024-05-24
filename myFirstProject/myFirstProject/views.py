from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from .models import Photo, Category, TagPost
from .forms import AddPostForm
from .utils import DataMixin
import uuid
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    data = {
        'content': 'Топ рейтинга!',
        'title': 'главная страница',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас', 'key_5': 'Добавить картинку'}
    }
    return render(request, 'myFirstProject/index.html', data)


@login_required
def about(request):
    data = {
        'content': 'О нас',
        'title': 'О нас',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас', 'key_5': 'Добавить картинку'}
    }
    return render(request, 'myFirstProject/about.html', data)


def comp( request):
    data = {
        'content': 'Сравнение',
        'title': 'Сравнение',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас', 'key_5': 'Добавить картинку'}
    }
    return render(request, 'myFirstProject/compare.html', data)


class PhotosHome(DataMixin, ListView):
    template_name = 'myFirstProject/photos.html'
    context_object_name = 'posts'
    title_page = 'Картинки'
    cat_selected = 0
    def get_queryset(self):
        return Photo.published.all().select_related('cat')


class ShowPost(DataMixin, DetailView):
    template_name = 'myFirstProject/photo.html'
    slug_url_kwarg = 'photo_slug'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, points=context['photo'].points, IMG=context['photo'].content,
                                      title=context['photo'].title, content='Картинка')

    def get_object(self, queryset=None):
        return get_object_or_404(Photo.published, slug=self.kwargs[self.slug_url_kwarg])


class PhotosCategory(DataMixin, ListView):
    template_name = 'myFirstProject/photos.html'
    context_object_name = 'posts'
    content_page = 'Картинки'
    allow_empty = False
    def get_queryset(self):
        return Photo.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория -' + cat.name,
                                      cat_selected=cat.pk,
                                      )


class TagPostList(DataMixin, ListView):
    template_name = 'myFirstProject/photos.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)

    def get_queryset(self):
        return Photo.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'myFirstProject/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление фото'
    permission_required = 'myFirstProject.add_photo'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.site_user = self.request.user
        return super().form_valid(form)


class UpdatePage(PermissionRequiredMixin,DataMixin, UpdateView):
    model = Photo
    fields = ['title',  'content', 'is_published', 'cat']
    template_name = 'myFirstProject/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование фото'
    permission_required = 'myFirstProject.change_photo'


# @permission_required(perm='myFirstProject.view_photo',raise_exception=True)
# def contact(request):
#     return HttpResponse("Обратная связь")


class DeletePage(DataMixin, DeleteView):
    model = Photo
    template_name = 'myFirstProject/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Удаление записи'


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
