from django.shortcuts import render
from django.http import HttpRequest

def show_main(request: HttpRequest):
    context = {
        'npm': '2406414536',
        'name': 'Dion Wisdom Pasaribu',
        'class': 'PBP F',
    }
    return render(request, "main.html", context)

# Create your views here.