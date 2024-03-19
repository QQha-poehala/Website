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
    content = models.ImageField(upload_to='img')
    place = models.IntegerField()
    points = models.IntegerField()
    tim_create = models.DateTimeField(auto_now_add=True)
    tim_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

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
