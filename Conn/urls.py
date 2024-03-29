"""Conn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from User.views import registartion_view, login_view, logout_view, main
from Profile.views import profile_view, post_view
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('registration/', registartion_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('<str:username>/', profile_view),
    path('<str:username>/status/<int:id>', post_view, name='post-view'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
