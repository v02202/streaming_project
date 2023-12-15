from django.urls import path

from . import views

urlpatterns = [
    path("subscribe_list", views.choose_channel, name='subscribe_list'),
    path("playlist_list/<str:streamer_key>", views.get_playlist_view, name='get_playlist_view'),
    path("stream_list/<str:playlist_id>", views.get_stream_list_view, name='get_stream_list_view')
]