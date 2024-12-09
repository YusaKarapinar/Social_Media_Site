# MessagePage/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Mesajlar Sayfası Görünümü
@login_required(login_url='/login/')
def message_page(request):
    messages = [
        {'sender': 'Alice', 'message': 'Hello!'},
        {'sender': 'Bob', 'message': 'How are you doing?'},
        {'sender': 'Charlie', 'message': 'Good Morning!'}
    ]
    return render(request, 'message/message_page.html', {
        'page_title': 'Messages',
        'messages': messages,
    })
