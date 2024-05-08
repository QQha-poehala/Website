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
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('compare', views.comp, name='compare'),
    path('photos', views.PhotosHome.as_view(), name='photos'),
    path('photos/<slug:photo_slug>/', views.ShowPost.as_view(), name='photo'),
    path('category/<slug:cat_slug>/', views.PhotosCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('del/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Фотографии для сравнения"
