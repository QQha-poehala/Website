from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д':
        'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и':
             'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п':
             'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х':
             'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y',
         'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Photo.Status.PUBLISHED)


class Photo(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    content = models.ImageField(upload_to='media/img', null=True, blank=True, verbose_name="Фото")
    place = models.IntegerField(verbose_name="Место")
    points = models.IntegerField(verbose_name="Очки")
    tim_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    tim_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категория")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name="Тэг")
    author = models.OneToOneField('Author', on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name='pho', verbose_name="Автор")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список фотографий"
        verbose_name_plural = "Список фотографий"
        ordering = ['tim_create']
        indexes = [
            models.Index(fields=['tim_create']),
        ]

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    photo_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
