from . import views
from django.urls import path
urlpatterns = [
    path('', views.blog , name="blog"),
    path('blogpost/<int:id>', views.blogpost , name="blogpost")
]
