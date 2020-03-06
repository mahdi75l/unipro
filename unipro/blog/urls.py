from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:category>', views.GetPostCategory, name='GetPostCategory'),
    path('news/', views.News, name='News'),
    path('news/loadMorePost', views.loadMorePost, name='NewsLoader'),
    path('news/<str:post_news>', views.detail_news, name='details'),

]