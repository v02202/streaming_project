# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os, datetime
from dotenv import load_dotenv
from django.http import JsonResponse, HttpResponse
from django.contrib.sessions.exceptions import SessionInterrupted
from .models import *
from ..favorite.models import mergeFavoriteAndSub
from django.template import loader
from django.shortcuts import render, redirect
from ..index import MAX_AGE

load_dotenv()

max_age = MAX_AGE


def choose_channel(request):
    if request.method == 'GET':
        youtube_oauth = request.COOKIES.get('youtube_oauth')
        print('---- Get cookie: %s -----' % (youtube_oauth))
        # subscribe_list, credentials = get_subscribe_list(youtube_oauth)
        subscribe_list, credentials = mergeFavoriteAndSub(request.user.id, youtube_oauth)
        template = loader.get_template('./stream/streamer_list.html')
        response = HttpResponse(
            template.render({'subscribe_list': subscribe_list}, request)
        )
        response.set_cookie(
            'youtube_oauth', 
            credentials,
            max_age=max_age,
            expires=datetime.datetime.strftime(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
        )
        return response
    
    elif request.method == 'POST':
        if request.POST.get('follow', None):
            stream_id = request.POST['follow']
            store_favorite_streamer(stream_id, request.user.id)
        elif request.POST.get('remove', None):
            stream_id = request.POST['remove']
            print(stream_id)
            remove_favorite_streamer(stream_id, request.user.id)
        return redirect("/api/stream/subscribe_list")

def get_playlist_list(youtube_oauth, streamer_key):
    stream_obj = StreamClass(youtube_oauth)
    if youtube_oauth is None:
        youtube_oauth = stream_obj.get_credentials()
    stream_obj.create_service()
    response, credentials = stream_obj.getStreamPlaylistList(streamer_key)
    return response, credentials

def get_playlist_view(request, streamer_key):
    if request.method == 'GET':
        youtube_oauth = request.COOKIES.get('youtube_oauth')
        stream_list, credentials = get_playlist_list(youtube_oauth, streamer_key)
        render_list = []
        if len(stream_list['items']) >0:
            for stream in stream_list['items']:
                render_dict = {
                    'streamer_title': stream['snippet']['channelTitle'],
                    'playlist_title': stream['snippet']['title'],
                    'thumbnails_url': stream['snippet']['thumbnails']['medium']['url'],
                    'video_src':f"https://www.youtube.com/playlist?list={stream['id']}"
                }
                render_list.append(render_dict)
        template = loader.get_template('./stream/playlist_list.html')
        response = HttpResponse(
            template.render({'render_list': render_list}, request)
        )
        response.set_cookie(
            'youtube_oauth', 
            credentials,
            max_age=max_age,
            expires=datetime.datetime.strftime(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
        )
        return response
    
def get_stream_list(youtube_oauth, playlist_id):
    stream_obj = StreamClass(youtube_oauth)
    if youtube_oauth is None:
        youtube_oauth = stream_obj.get_credentials()
    stream_obj.create_service()
    response, credentials = stream_obj.getStreamList(playlist_id)
    return response, credentials

def get_stream_list_view(request, playlist_id):
    if request.method == 'GET':
        youtube_oauth = request.COOKIES.get('youtube_oauth')
        stream_list, credentials = get_stream_list(youtube_oauth, playlist_id)
        render_list = []
        if len(stream_list['items']) >0:
            # render_dict = {
            #         'video_title': stream_list['items'][0]['snippet']['title'],
            #         'video_src':f"https://www.youtube.com/embed/{stream_list['items'][0]['snippet']['channelId']}?si=JlnLuzfcSgNTiErB"
            #     }
            for stream in stream_list['items']:
                render_dict = {
                    'video_title': stream['snippet']['title'],
                    'video_src':f"https://www.youtube.com/embed/{stream['snippet']['channelId']}?si=JlnLuzfcSgNTiErB"
                }
                print('test ------ ', render_dict)
                render_list.append(render_dict)
        template = loader.get_template('./stream/stream_list.html')
        response = HttpResponse(
            template.render({'render_list': render_list}, request)
        )
        response.set_cookie(
            'youtube_oauth', 
            credentials,
            max_age=max_age,
            expires=datetime.datetime.strftime(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
        )
        return response