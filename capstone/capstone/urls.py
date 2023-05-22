"""
URL configuration for capstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from toilet.views import fetch_and_save_toilet_data
from toilet.views import create_toilet
from toilet.views import get_toilet
from toilet.views import get_all_toilets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/toilet/post/', fetch_and_save_toilet_data, name = 'fetch_toilet_data'),
    path('', fetch_and_save_toilet_data, name='empty_path'),
    path('api/toilet/create/', create_toilet, name='create_toilet'),
    path('api/toilet/<int:toilet_id>/', get_toilet, name='get_toilet'),
    path('api/toilet/', get_all_toilets, name='get_all_toilets'),

]
