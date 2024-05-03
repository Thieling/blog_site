from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def view_home(request):
    return render(request, "blog_web/base.html")

