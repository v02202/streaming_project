from django.contrib import admin

# Register your models here.
from .models import Users, Label, Stream, Streamer, Streamer_group, Favorite
admin.site.register(Users)  #註冊至Administration(管理員後台)
admin.site.register(Label) 
admin.site.register(Stream)
admin.site.register(Streamer) 
admin.site.register(Streamer_group) 
admin.site.register(Favorite)