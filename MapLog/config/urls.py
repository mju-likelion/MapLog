from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # django apps
    # core
    path("", include("core.urls", namespace="core")),
    # users
    path("users/", include("users.urls", namespace="users")),
    # posts
    path("posts/", include("posts.urls", namespace="posts")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
