from django.http import HttpResponse

from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

