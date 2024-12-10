from django.shortcuts import render
from HomePage.models import Post

def feed_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed/feed_page.html', {'posts': posts})
