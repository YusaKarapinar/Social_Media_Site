from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def FeedPage(req):
    return render(req,'HomePage/index.html')


