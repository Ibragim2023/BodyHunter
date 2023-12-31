from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from bodyapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bodyapp.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

handler404 = notFound404