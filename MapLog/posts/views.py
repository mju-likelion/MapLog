import requests, json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Posts


def new_post(request):
    posts = Posts.objects
    return render(request, "posts/post_create.html", {"posts": posts})


def post_detail(request, post_id):
    details = get_object_or_404(Posts, pk=post_id)
    return render(request, "posts/post_detail.html", {"details": details})


def post_create(request):
    post = Posts()

    post.lat = request.POST.get("lat_form")
    post.lng = request.POST.get("lng_form")

    post.title = request.POST.get("title")
    post.pick_date = request.POST.get("pick_date")
    post.create_date = timezone.datetime.now()
    post.music = request.POST.get("music")
    post.mood = request.POST.get("mood")
    post.description = request.POST.get("description")
    post.image = request.FILES["image"]  # views.py 업로드오류 해결

    post.save()
    return redirect("/posts/" + str(post.id))  # config URL오류나서 맞춰서 수정


def getApi(request):
    report = Posts.objects.all()
    report_list = serializers.serialize("json", report)
    return HttpResponse(report_list, content_type="text/json-comment-filtered")


def apiTest(request):
    return render(request, "posts/apiTest.html")


# def post_list(request):
#     posts = Posts.objects.all()
#     context = {"posts": posts, "posts_js": json.dumps([post.json() for post in posts])}
#     return render(request, "map_marker.html", context)


# def post_update(request):


def map_search(request):
    return render(request, "posts/map_search.html")


def map_marker(request):
    return render(request, "posts/map_marker.html")
