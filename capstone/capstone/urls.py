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

from toilet.views import fetch_and_save_toilet_data, create_toilet #C
from toilet.views import get_toilet, get_all_toilets #R
from toilet.views import update_toilet #U
from toilet.views import delete_toilet #D
from toilet.views import create_review
from toilet.views import get_review
from toilet.views import update_review
from toilet.views import delete_review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/toilet/post/', fetch_and_save_toilet_data, name='fetch_toilet_data'),
    path('api/toilet/create/', create_toilet, name='create_toilet'),
    path('api/toilet/', get_toilet, name='get_toilet'),
    path('api/toilet/all/', get_all_toilets, name='get_all_toilets'),
    path('api/toilet/update/', update_toilet, name='update_toilet'),
    path('api/toilet/delete/', delete_toilet, name='delete_toilet'),
    path('api/review/post/', create_review, name = 'create_review'),
    path('api/review/get/', get_review, name = 'get_review'),
    path('api/review/update/', update_review, name = 'update_review'),
    path('api/review/delete/', delete_review, name = 'delete_review')
]
