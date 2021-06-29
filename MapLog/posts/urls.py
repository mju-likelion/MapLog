from django.urls import path
from django.conf import settings
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("new/", post_views.new_post, name="new_post"),
    path("create/", post_views.post_create, name="post_create"),
    path("<int:post_id>", post_views.post_detail, name="post_detail"),
    path("map/search", post_views.map_search, name="map_search"),
    path("map/marker", post_views.map_marker, name="map_marker"),
]
