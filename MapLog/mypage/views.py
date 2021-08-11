from posts.views import post_create
from abc import ABCMeta
from os import curdir, startfile
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import By_date
from posts.models import Posts
from datetime import datetime, timedelta
import json

# MY PAGE
def by_date(request):
    by_date = By_date()
    data = []
    posts = Posts.objects.all().order_by('pick_date')
    by_date.start_date = request.POST.get("start_date")
    by_date.end_date = request.POST.get("end_date")
    print(by_date.start_date)
    print(by_date.end_date)
    by_date.save() 

    for post in posts:
      dict_data = {
        "pick_date" : post.pick_date.isoformat(), # datetime 객체를 yyyy-mm-dd 형식으로 변환
        "image" : post.image.url,
      }
      data.append(dict_data)

    print(data)
    context = {
        "data" : data,
        "start_date" : by_date.start_date, 
        "end_date" : by_date.end_date, 
    }
    return render(request, "../templates/menu/mypage/by_date.html", context)


def acc_info(request):
    return render(request, "../templates/menu/mypage/acc_info.html", {"acc_info": acc_info})

def by_mood(request):
    return render(request, "../templates/menu/mypage/by_mood.html", {"by_mood": by_mood})

def getApi2(request):
    report2 = By_date.objects.all()
    report2_list = serializers.serialize("json", report2)
    return HttpResponse(report2_list, content_type="text/json-comment-filtered")


def apiTest2(request):
    return render(request, "menu/mypage/apiTest2.html")

