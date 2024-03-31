from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Photo, Category, TagPost


def index(request):
    data = {
        'content': 'Топ рейтинга!',
        'title': 'главная страница',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'}
    }
    return render(request, 'myFirstProject/index.html', data)


def about(request):
    data = {
        'content': 'О нас',
        'title': 'О нас',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'}
    }
    return render(request, 'myFirstProject/about.html', data)


def comp(request):
    data = {
        'content': 'Сравнение',
        'title': 'Сравнение',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'}
    }
    return render(request, 'myFirstProject/compare.html', data)


def photos(request):
    photos = Photo.published.all()

    data = {
        'content': 'Картинки',
        'title': 'Картинки',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'posts': photos,
        'cat_selected': 0,
    }
    return render(request, 'myFirstProject/photos.html', data)


def show_photo(request, photo_slug):
    photo = get_object_or_404(Photo, slug=photo_slug)

    data = {
        'title': photo.title,
        'content': 'Картинка',
        'points': photo.points,
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'IMG': photo.content,
        'photo': photo,
        'cat_selected': 1,
    }
    return render(request, 'myFirstProject/photo.html', data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Photo.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика:{category.name}',
        'posts': posts,
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'cat_selected': category.pk,
    }
    return render(request, 'myFirstProject/photos.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Photo.Status.PUBLISHED)

    data = {
        'title': f'Тег:{tag.tag}',
        'posts': posts,
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'cat_selected': None,
    }
    return render(request, 'myFirstProject/photos.html', context=data)


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
