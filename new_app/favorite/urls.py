from django.urls import path

from . import views

urlpatterns = [
    path("streamer", views.get_favorite_streamer, name='get_favorite_streamer'),
]