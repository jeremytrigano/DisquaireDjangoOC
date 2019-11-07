from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', include(('store.urls', 'store'), namespace='store')),
    path('idman/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
