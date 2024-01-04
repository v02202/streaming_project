from django.urls import path

from . import views

urlpatterns = [
    path("list", views.get_users, name = 'get_users'),
    # path("logout", views.logout_view),
]