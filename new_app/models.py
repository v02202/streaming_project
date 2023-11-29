from django.db import models

# Create your models here.
class Users(models.Model):
    users_oid = models.BigAutoField(primary_key=True)
    users_id = models.BigIntegerField(blank=False)
    users_email = models.EmailField(max_length=211, blank=False)
    users_name = models.CharField(max_length=100, blank=True)
    users_key = models.CharField(max_length=20, blank=False)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)


class Label(models.Model):
    label_oid = models.BigAutoField(primary_key=True)
    label_id = models.BigIntegerField(blank=False)
    label_name = models.CharField(max_length=50, blank=True)
    stream_oid = models.ForeignKey(
        "Stream",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
    )
    is_share = models.BooleanField(default = 'false')
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)


class Stream(models.Model):
    stream_oid = models.BigAutoField(primary_key=True)
    stream_id = models.BigIntegerField(blank=False)
    stream_api_key = models.CharField(max_length=20, blank=False)
    streamer_oid = models.ForeignKey(
        "Streamer",
        on_delete=models.CASCADE,
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Streamer(models.Model):
    streamer_oid = models.BigAutoField(primary_key=True)
    streamer_id = models.BigIntegerField(blank=False)
    streamer_api_key = models.CharField(max_length=20, blank=False)
    streamer_group_oid = models.ForeignKey(
        "Streamer_group",
        on_delete=models.CASCADE,
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Streamer_group(models.Model):
    streamer_group_oid = models.BigAutoField(primary_key=True)
    streamer_group_id = models.BigIntegerField(blank=False)
    streamer_group_name = models.CharField(max_length=50, blank=False)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

class Favorite(models.Model):
    favorite_oid = models.BigAutoField(primary_key=True)
    favorite_id = models.BigIntegerField(blank=False)
    users_oid = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
    )
    streamer_oid = models.ForeignKey(
        "Streamer",
        on_delete=models.CASCADE,
    )
    stream_oid = models.ForeignKey(
        "Stream",
        on_delete=models.CASCADE,
    )
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
