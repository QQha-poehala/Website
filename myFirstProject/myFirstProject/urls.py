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
    path('compare', views.comp, name='compare'),
    path('photos', views.photos, name='photos'),
    path('photos/<slug:photo_slug>/', views.photo, name='photo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
