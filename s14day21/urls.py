"""s14day21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', views.index, {'name': 'alex'}),
    path('a/', include('app01.urls', namespace='author')),
    path('text/', include('app01.urls')),
    re_path('login/', views.login_1),
    re_path('index/', views.index_1),
]
