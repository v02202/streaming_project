# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from django.http import JsonResponse
from .models import StreamClass
load_dotenv()
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_service_name = os.environ.get("API_SERVICE_NAME")
api_version = os.environ.get("API_VERSION")
client_secrets_file =  './client_secret_456715957369-o0epqn9ha9m2hme6r6qmiavo47ehm05v.apps.googleusercontent.com.json'



async def getSubscribeList(request):
    youtube_service = await StreamClass.create_service()
    response = await StreamClass.getSubscribeList(youtube_service)
    return JsonResponse(response)




