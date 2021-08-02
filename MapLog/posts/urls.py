from django.urls import path
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("new/", post_views.new_post, name="new_post"),
    path("create/", post_views.post_create, name="post_create"),
    path("<int:post_id>", post_views.post_detail, name="post_detail"),
    #추가 : 로그 수정 path
    path("update/<int:post_id>", post_views.post_update, name="post_update"),
    #추가 : 로그 삭제 path
    #path("delete/<int:post_id>", post_views.post_delete, name="post_delete"),
    path("map/search", post_views.map_search, name="map_search"),
    path("map/marker", post_views.map_marker, name="map_marker"),
    path("getApi/", post_views.getApi, name="getApi"),
    path("apiTest/", post_views.apiTest, name="apiTest"),
]
