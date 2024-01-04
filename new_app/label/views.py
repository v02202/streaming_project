from django.contrib.auth.decorators import login_required
from .models import *
from ..stream.models import store_stream, DevelopYoutubeClass
from ..users.models import get_user_obj
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
import re

@login_required
def store_label(request):
    if request.method == 'POST':
        form = LableForm(request.POST)
        if form.is_valid():
            print('request.POST', request.POST)
            timestamp_url = request.POST['timestamp_url']
            timestamp_list = re.split(r'(\w{11})\?t=(\d*)$', timestamp_url)
            if len(timestamp_list) != 0:
                stream_api_key = timestamp_list[1]
                timestamp = int(timestamp_list[2])
                
                service = DevelopYoutubeClass()
                response = service.getStreamDetail(stream_api_key)
                streamer_key = response['items'][0]['snippet']['channelId']
                stream_obj = store_stream(stream_api_key, streamer_key)
                print('stream_api_key %s timestamp %s  request.user.id %s' % (stream_api_key, timestamp, request.user.id))
                cache_form = form.save(commit=False)
                cache_form.owner = get_user_obj(request.user.id)
                cache_form.stream_oid = stream_obj
                cache_form.timestamp = timestamp
                cache_form.save()

            return redirect("/api/label/store_label")
    else:
        form = LableForm()
    template = loader.get_template('./label/store_label.html')
    return HttpResponse(template.render({"form": form}, request))



@login_required
def get_label(request):
    if request.method == 'GET':
        detail_list = get_label_list(request.user.id)
        template = loader.get_template('./label/get_label.html')
        return HttpResponse(template.render({'detail_list':detail_list}, request))
        
