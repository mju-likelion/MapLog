from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include("users.urls", namespace="login")),
    path("posts/", include("posts.urls", namespace="posts")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
