from django.urls import path

from . import views

urlpatterns = [
    path("subscribe_list", views.chooseChannel, name='subscribe_list'),
    path("stream_list/<str:streamer_key>", views.getChannelListView, name='stream_list')
]