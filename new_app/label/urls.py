from django.urls import path

from . import views

urlpatterns = [
    path("store_label", views.store_label, name='store_label'),
    path("get_label", views.get_label, name='get_label'),
]