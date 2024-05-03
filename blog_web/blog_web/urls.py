from django.contrib import admin
from django.urls import path, include
from .views import view_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view_home, name="home"),
    path("blog/", include('blog_web.blog.urls')),
]