from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Photo.Status.PUBLISHED)


class Photo(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.ImageField(upload_to='media/img', null = True, blank=True)
    place = models.IntegerField()
    points = models.IntegerField()
    tim_create = models.DateTimeField(auto_now_add=True)
    tim_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    author = models.OneToOneField('Author', on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name='pho')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['tim_create']
        indexes = [
            models.Index(fields=['tim_create']),
        ]

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

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
