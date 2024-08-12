from django.contrib import admin
from django.urls import path
from .views import ShortnerListAPIView,ShortnerCreateAPIView 


urlpatterns = [
   path('', ShortnerListAPIView.as_view(), name='all_links'),
   path('create/', ShortnerCreateAPIView.as_view(), name='create_api'),
    
]