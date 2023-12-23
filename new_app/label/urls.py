from django.urls import path

from . import views

urlpatterns = [
    path("store_label", views.store_label, name='store_label'),
]