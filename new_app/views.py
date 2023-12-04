from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import loader
# Create your views here.



def homepage_view(request):
  template = loader.get_template('hello.html')
  context = {
    'now': datetime.datetime.now().strftime("%H:%M:%S"),
  }
  return HttpResponse(template.render(context, request))   