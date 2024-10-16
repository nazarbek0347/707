from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings



urlpatterns = [
    # your other url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_707.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)