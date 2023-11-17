from food_app import views
from django.urls import path
# from .load_food import run
urlpatterns = [
    path('index/', views.index ,name="index"),
    path('index/view_food/<int:FoodID>/',views.view_food,name="view_food"),
    path('recommend/',views.recommend,name="recommend"),
    path('popular_food/',views.popular_food,name="popular_food"),
    path('recommend_food/',views.recommend_food,name="recommend_food"),
     path('about/', views.about ,name="about"),
    # path('load/',run,name='load'),
]
