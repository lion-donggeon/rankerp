from django.contrib import admin
from django.urls import path, include
from main.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),
    path('main/', include('main.urls')),
    path('common/', include('common.urls')),
    path('post/', include('post.urls')),
]


handler404 = 'common.views.page_not_found'


# Summernote 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [path('summernote/', include('django_summernote.urls'))]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)