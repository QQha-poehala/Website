from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Photo


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
    }
    return render(request, 'myFirstProject/photos.html', data)


def photo(request, photo_slug):
    photo = get_object_or_404(Photo, slug=photo_slug)

    data = {
        'title': photo.title,
        'content': 'Картинка',
        'name': photo.title,
        'points': photo.points,
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'IMG': photo.content,
    }
    return render(request, 'myFirstProject/photo.html', data)


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
