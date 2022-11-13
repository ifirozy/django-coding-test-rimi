
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('product/', include('product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
