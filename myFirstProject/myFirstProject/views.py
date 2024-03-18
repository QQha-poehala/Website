from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


data_db = [
    {'id': 1, 'title': 'леопард', 'content': 'фото', 'is_published': True},
    {'id': 2, 'title': 'котик', 'content': 'фото', 'is_published': True},
    {'id': 3, 'title': 'бурундук', 'content': 'фото', 'is_published': False},
    {'id': 4, 'title': 'лоси', 'content': 'фото', 'is_published': True},
]


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
    data = {
        'content': 'Картинки',
        'title': 'Картинки',
        'dict': {'key_1': 'Главная', 'key_2': 'Сравнить!', 'key_3': 'Картинки', 'key_4': 'Про нас'},
        'posts': data_db,
    }
    return render(request, 'myFirstProject/photos.html', data)


def photo(request, photo_id):

    if photo_id > 25:
        return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
    return HttpResponse(f"<h1>фото </h1><p >id:{photo_id}</p>")


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
