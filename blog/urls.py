from django.urls import path, include
from blog import views
from . import views

from django.conf import settings
from django.conf.urls.static import static


from .views import *






app_name = 'blog'

urlpatterns = [
    
    path('', views.index, name="index"),
]