from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post # .model - bo jest w tym samym folderze

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog home</h1>')
    print(request)
    return render(request,'blog/home.html',context) # w html odnosimy sie nie do contex ale do posts

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
