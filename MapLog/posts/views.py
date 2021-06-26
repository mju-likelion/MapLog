import requests
from django.shortcuts import render
from .models import Posts

def post_create(request):
    if request.method == 'GET':
        posts = Posts.objects
        return render(request, "posts/post_create.html", {'posts': posts})
    # elif request.method == 'POST':
    #     title = request.POST['title']
    #     pick_date = request.POST['pick_date']
    #     create_date = request.POST['create_date']
    #     music = request.POST['music']
    #     mood = request.POST['mood']
    #     description = request.POST['description']
    #     image = request.FILES['image']

    #     new_post = Posts.objects.create(title=title, pick_date=pick_date, create_date=create_date, music=music, mood=mood, description=description, image=image)


# def post_update(request):

