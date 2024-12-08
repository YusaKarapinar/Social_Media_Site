from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def MessageFunc(req):
    return HttpResponse('Message Func Return')