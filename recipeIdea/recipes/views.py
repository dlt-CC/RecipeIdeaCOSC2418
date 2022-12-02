from django.views import generic
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def Register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def Login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())