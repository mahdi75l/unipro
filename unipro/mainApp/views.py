import os

from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
from blog.models import Post
from mainApp.models import Guid, CategoryGuid
from unipro import settings


def home(request):
    posts = Post.objects.all()[:9]
    return render(request, "index.html",{"posts":posts})


def aboutUs(request):
    return render(request, "aboutUs.html")


def matches(request):
    return render(request, "matches.html")


def Roll(request):
    allpost = Guid.objects.all()
    allcategory = CategoryGuid.objects.all()
    return render(request, "Roll.html",{"allpost":allpost , "allcategory":allcategory})


def contactUs(request):
    return render(request, "contactUs.html")


def downloadG(request,url):
    file_path = os.path.join(settings.MEDIA_ROOT, url)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        raise Http404
