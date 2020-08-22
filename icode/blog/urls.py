from django.urls import path, include
from blog import views

urlpatterns = [
    path('postComment', views.commentPost, name='commentPost'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]