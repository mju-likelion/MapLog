from django.shortcuts import render


def about_us(request):
    return render(request, "menu/about_us.html")

def support(request):
    return render(request, "menu/support.html")
