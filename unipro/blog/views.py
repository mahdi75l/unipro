from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from blog.Class import Example
from django.db.models import Q
import json

# Create your views here.
from blog.models import Post, Category, Comment


def Home(request):
    post = Category.objects.all()[:9]
    return HttpResponse(post)


def GetPostCategory(request, category):
    List = Example.getPostCategory(category)
    return HttpResponse(List)


def News(request):
    categories = Category.objects.all()
    page = 0
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    first = page * 9
    end = first + 9
    page += 1

    if request.GET:
        if request.GET.get('state'):
            state = int(request.GET.get('state'))
        if state != 0 and request.GET.get('text'):
            text = request.GET.get('text')
            news = Post.objects.filter(category=state).filter(
                Q(body__contains=text) | Q(title__contains=text) | Q(abstract__contains=text))[
                   first:end]
            return render(request, "News.html", {"posts": news, "text": text, "state": state, "categories": categories
                , "page": page})
        else:
            if not state == 0:
                news = Post.objects.filter(category=state)[first:end]
                return render(request, "News.html",
                              {"posts": news, "text": "", "categories": categories, "state": state, "page": page})
            else:
                news = Post.objects.all()[first:end]
                return render(request, "News.html", {"posts": news, "state": 0, "categories": categories, "page": page})

    else:
        news = Post.objects.all()[first:end]
        return render(request, "News.html", {"posts": news, "categories": categories, "page": 1, "state": 0})


def detail_news(request, post_news):
    news = get_object_or_404(Post, slug=post_news)
    return render(request, "detail-news.html", {"post": news})


def loadMorePost(request):
    if request.is_ajax() and request.GET:
        page = int(request.GET.get('page'))
        first = page * 9
        end = first + 9
        page += 1
        state = int(request.GET.get('state'))
        text = request.GET.get('text')
        if text:
            news = Post.objects.filter(category=state).filter(
                Q(body__contains=text) | Q(title__contains=text) | Q(abstract__contains=text))[
                   first:end]
        else:
            if not state == 0:
                news = Post.objects.filter(category=state)[first:end]
            else:
                news = Post.objects.all()[first:end]
        data = list(news.values())
        return JsonResponse(data, safe=False)
