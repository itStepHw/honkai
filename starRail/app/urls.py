from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('worlds', Worlds.as_view(), name='worlds'),
]