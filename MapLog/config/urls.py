from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include("login.urls", namespace="login")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
