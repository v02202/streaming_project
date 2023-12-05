from django.urls import path

from . import views

urlpatterns = [
    path("subscribe_list", views.getSubscribeList)
]