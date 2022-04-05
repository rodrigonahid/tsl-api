from django.contrib import admin
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('users.urls', namespace='users')),
]
