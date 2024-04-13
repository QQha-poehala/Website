from django.contrib import admin, messages
from .models import Photo, Category


class AuthorFilter(admin.SimpleListFilter):
    title = 'Статус фотографии'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('author', 'Есть автор'),
            ('unknown', 'Нет автора'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'author':
            return queryset.filter(author__isnull=False)
        elif self.value() == 'unknown':
            return queryset.filter(author__isnull=True)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'cat', 'author', 'tags']
    #exclude = ['tags', 'is_published']
    #readonly_fields = ['slug']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ['tags']
    list_display = ('title', 'tim_create', 'is_published', 'cat', 'info')
    list_display_links = ('title', )
    ordering = ['tim_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    list_filter = [AuthorFilter, 'cat__name', 'is_published']

    @admin.display(description="Описание", ordering='content')
    def info(self, photo: Photo):
        return f"Описание {len(photo.content)} символ."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Photo.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Photo.Status.DRAFT)
        self.message_user(request, f" {count} записей снято с публикации.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
