import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Posts


def new_post(request):
    posts = Posts.objects
    return render(request, "posts/post_create.html", {"posts": posts})


def detail(request, post_id):
    details = get_object_or_404(Posts, pk=post_id)
    return render(request, "post_detail.html", {"details": details})


def post_create(request):
    post = Posts()

    post.title = request.GET["title"]
    post.pick_date = request.GET["pick_date"]
    post.create_date = timezone.datetime.now()
    post.music = request.GET["music"]
    post.mood = request.GET["mood"]
    post.description = request.GET["description"]
    post.image = request.FILES["image"]

    post.save()

    return redirect("/post/" + str(post.id))


# def post_update(request):
