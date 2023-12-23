from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class Label(models.Model):
    label_oid = models.BigAutoField(primary_key=True)
    label_name = models.CharField(max_length=50, blank=True)
    timestamp = models.IntegerField(blank=False)
    stream_oid = models.ForeignKey(
        "Stream",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    is_share = models.BooleanField(default = 'false')
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)


class Stream(models.Model):
    stream_oid = models.BigAutoField(primary_key=True)
    stream_api_key = models.CharField(max_length=20, blank=False)
    streamer_oid = models.ForeignKey(
        "Streamer",
        on_delete=models.CASCADE,
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Streamer(models.Model):
    streamer_oid = models.BigAutoField(primary_key=True)
    streamer_api_key = models.CharField(max_length=20, blank=False)
    streamer_group_oid = models.ForeignKey(
        "Streamer_group",
        on_delete=models.CASCADE,
        null=True
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Streamer_group(models.Model):
    streamer_group_oid = models.BigAutoField(primary_key=True)
    streamer_group_name = models.CharField(max_length=50, blank=False)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Favorite(models.Model):
    favorite_oid = models.BigAutoField(primary_key=True)
    users_oid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    streamer_oid = models.ForeignKey(
        "Streamer",
        on_delete=models.CASCADE,
        null=True
    )
    stream_oid = models.ForeignKey(
        "Stream",
        on_delete=models.CASCADE,
        null=True
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
