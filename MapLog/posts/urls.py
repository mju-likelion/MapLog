from django.urls import path
from django.conf import settings
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("create/", post_views.post_create, name="post_create"),
]
