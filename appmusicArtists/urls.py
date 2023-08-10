from django.contrib import admin
from django.urls import path

from .views import show_categories, show_all_artists, show_more

urlpatterns = [
    path('', show_categories),
    path('<str:genre_name>/', show_all_artists),
    path('<str:genre_name>/<int:pk>/', show_more)
]