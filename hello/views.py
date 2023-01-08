from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Hello, Django!")
# Create your views here.

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )