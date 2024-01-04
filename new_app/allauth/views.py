from datetime import datetime
from django.shortcuts import render

def login_homepage(request):
    return render(request, "./base.html")