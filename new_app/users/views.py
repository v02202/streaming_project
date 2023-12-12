from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core import serializers
from django.template import loader





def logout_view(request):
    logout(request)
    return redirect("/")


def get_users(request):
    if request.user.is_authenticated:
        context = {
            'user_id':request.user.id,
            'user_name':request.user.username,
            'user_email':request.user.email
        }
        template = loader.get_template('./stream/user_list.html')
        return HttpResponse(template.render(context, request))  
    else:
        return HttpResponseBadRequest("please login")