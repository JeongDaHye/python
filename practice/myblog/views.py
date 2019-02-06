from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Myblog

def home(request): 
  blogs = Myblog.objects
  return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id): 
  blog_detail = get_object_or_404(Myblog, pk = blog_id)
  return render(request, 'detail.html', {'myblog':blog_detail})

def new(request): #new.html을 띄워주는 함수
  return render(request, 'new.html')

def create(request):
    myblog = Myblog()
    myblog.title = request.GET['title']
    myblog.body = request.GET['body']
    myblog.pub_date = timezone.datetime.now()
    myblog.save()
    return redirect('/myblog/' + str(myblog.id))
