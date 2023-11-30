from django.urls import path

from . import views

urlpatterns = [
    path("test", views.current_datetime),
    path("", views.home),
    path("logout", views.logout_view),
]