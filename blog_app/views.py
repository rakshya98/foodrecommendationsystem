from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def blog(request):
    blog=Blog.objects.all()
    
    return render(request,'blog_app/blogpost.html',{'blog':blog})

def __str__(self):
    return self.title

def blogpost(request, id):
    post = Blog.objects.filter(id=id).first()
    if not post:
        return HttpResponse("Blog post not found", status=404)
    return render(request, 'blog_app/post.html', {'post': post})
