"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_app.views import user_new, user_edit, user_delete, user_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_new/', user_new, name='user_new'),
    path('user_edit/<int:user_id>/', user_edit, name='user_edit'),
    path('user_delete/<int:user_id>/', user_delete, name='user_delete'),
    path('user_list/', user_list, name='user_list'),
]
