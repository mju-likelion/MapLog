from django.urls import path
from django.conf import settings
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("new/", post_views.new_post, name="new_post"),
    path("create/", post_views.post_create, name="post_create"),
    path("<int:post_id>", post_views.post_detail, name="post_detail"),
    path("map/", post_views.map_page, name="map_page")
]
