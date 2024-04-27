from django. contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

handler404 = 'myFirstProject.views.page404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('addpage', views.addpage, name='addpage'),
    path('compare', views.comp, name='compare'),
    path('photos', views.photos, name='photos'),
    path('photos/<slug:photo_slug>/', views.show_photo, name='photo'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Фотографии для сравнения"
