# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os, datetime
from dotenv import load_dotenv
from django.http import JsonResponse, HttpResponse
from django.contrib.sessions.exceptions import SessionInterrupted
from .models import *
from django.template import loader
from django.shortcuts import render, redirect
from ..index import MAX_AGE

load_dotenv()

max_age = MAX_AGE

def getSubscribeList(youtube_oauth):
    stream_obj = StreamClass(youtube_oauth)
    if youtube_oauth is None:
        youtube_oauth = stream_obj.get_credentials()
    stream_obj.create_service()
    response = stream_obj.getSubscribeList()
    return response


def chooseChannel(request):
    if request.method == 'GET':
        youtube_oauth = request.COOKIES.get('youtube_oauth')
        print('---- Get cookie: %s -----' % (youtube_oauth))
        subscribe_list = getSubscribeList(youtube_oauth)
        template = loader.get_template('./stream/stream_list.html')
        response = HttpResponse(
            template.render({'subscribe_list': subscribe_list['items']}, request)
        )
        response.set_cookie(
            'youtube_oauth', 
            youtube_oauth,
            max_age=max_age,
            expires=datetime.datetime.strftime(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
        )
        return response
    
    elif request.method == 'POST':
        stream_id = request.POST['follow']
        print(stream_id)
        favorite_oid = store_favorite_streamer(stream_id, request.user.id)

        return redirect("/api/stream/subscribe_list")
