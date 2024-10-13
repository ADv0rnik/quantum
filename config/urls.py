from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from qa.views import index

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('qa/', include('qa.urls', namespace='qa')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)