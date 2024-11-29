from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('auth_view.urls', 'auth_view') , namespace="auth")),
    path('' , include(('masyarakat_view.urls', 'masyarakat_view'), namespace="masyarakat")),
    path('petugas/', include(('petugas_view.urls', 'petugas_view'), namespace="petugas")),
    path('dinas/', include(('petugas_view.urls', 'petugas_view'), namespace="dinas")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
