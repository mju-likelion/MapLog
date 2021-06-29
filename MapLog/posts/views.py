import requests
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

    post.title = request.POST.get("title")
    post.pick_date = request.POST.get("pick_date")
    post.create_date = timezone.datetime.now()
    post.music = request.POST.get("music")
    post.mood = request.POST.get("mood")
    post.description = request.POST.get("description")
    post.image = request.POST.get("image")
    post.save()

    return redirect("/post/" + str(post.id))


# def post_update(request):


def map_search(request):
    return render(request, "posts/map_search.html")


def map_marker(request):
    return render(request, "posts/map_marker.html")
