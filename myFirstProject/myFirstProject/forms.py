from django import forms
from .models import Category, Author, Photo
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class RussianValidator:
    ALLOWED_CHARS ="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message,
                                  code=self.code, params={"value": value})


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категория")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Нет автора", required=False, label="Автор")
    class Meta:
        model = Photo
        fields = ['title', 'slug', 'content',
                  'cat', 'author', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title






