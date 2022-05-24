import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    data = {
        'account': '12345',
        'password': 'password',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def studentRegister(request):
    id=request.POST['id']
    print(id)
    return HttpResponse("yes")