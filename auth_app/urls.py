from django.urls import path,include
from auth_app import views
urlpatterns = [
    path('auth/register/',views.register,name='auth_app-register'),
    path('auth/login/',views.signin,name='auth_app-login'),
    path('auth/logout/',views.signout,name='auth_app-logout'),
     path('', views.signin, name='auth_app-login'),  
]