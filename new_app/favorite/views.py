from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse



@login_required
def get_favorite_streamer(request):
    if request.method == 'GET':
        streamer_list = getFavoriteStreamer(request.user.id)
        template = loader.get_template('./favorite/streamer.html')
        return HttpResponse(template.render({'streamer_list':streamer_list}, request))
        # return JsonResponse(serializers.serialize('json', detail_list), safe=False)