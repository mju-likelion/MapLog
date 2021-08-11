from django.urls import path
from . import views as mypage_views

app_name = "mypage"

urlpatterns = [
   
    # MY PAGE
    path("", mypage_views.acc_info, name="acc_info"),
    path("by_date/", mypage_views.by_date, name="by_date"),
    path("by_mood/", mypage_views.by_mood, name="by_mood"),
    # path("getApi2/", mypage_views.getApi2, name = "getApi2"),
    # path("apiTest2/", mypage_views.apiTest2, name = "apiTest2"),
    
]
