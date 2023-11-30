from django.http import HttpResponse, JsonResponse
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def current_datetime(request):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(now)
    return JsonResponse({'test_message':now})


def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

