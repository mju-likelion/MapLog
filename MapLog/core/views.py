from django.shortcuts import render


def main_page(request):
    return render(request, "main.html")


def about_us(request):
    return render(request, "menu/about_us.html")


def support(request):
    return render(request, "menu/support.html")
