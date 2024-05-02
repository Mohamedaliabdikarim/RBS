from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('login/', views.login_user, name='login'),
     path('logout/', views.logout_user, name='logout'),
     path('menu/', views.menu_list, name='menu'),
     path('register/', views.register_user, name='register'),
     path('add/', views.add_review, name='add_review'),
    path('review_list', views.review_list, name='review_list'),



]





