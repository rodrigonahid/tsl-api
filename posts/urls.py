from django.urls import path

from . import views

urlpatterns = [
  path('posts/', views.post_list ),
  path('posts/<str:title>/', views.post_detail ),

]