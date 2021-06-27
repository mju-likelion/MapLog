from django.urls import path
from django.conf import settings
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("create/", post_views.new_post, name="post_create"),
    path("<int:post_id>", post_views.detail, name="detail"),
]
