"""movie_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test1', test1),
    path('api/test2', test2),
    path('api/test3', test3),
    path('api/test4', test4),
    path('api/test5', test5),
    path('api/test6', test6),
    path('api/test7', test7),
    path('api/test8', test8),
    path('api/test9', test9),
    path('api/test10', test10),
    path('api/test11', test11),
    path('api/test12', test12),
]
