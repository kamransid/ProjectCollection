from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Posts

def index(request):
    
    posts = Posts.objects.all()[:10]
     
    contex = {
         'title':'Latest Post',
         'posts': posts
     }

    # return HttpResponse('HELLO FROM POST')
    return render(request, 'posts/index.html', contex)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'posts/details.html', context)
