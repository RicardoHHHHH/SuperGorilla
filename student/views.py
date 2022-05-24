import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'account': '12345',
        'password': 'we',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')