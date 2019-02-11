from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Myblog

def home(request): 
  blogs = Myblog.objects
  # 블로그 모든 글을 대상으로
  blog_list = Myblog.objects.all()
  # 블로그 객체를 5개를 한 페이지로 자르기
  paginator = Paginator(blog_list,3)
  # request된 페이지가 뭔지를 알아내고 
  page = request.GET.get('page')
  # request된 페이지를 얻어온 뒤 return 해 준다.
  posts = paginator.get_page(page)
  return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

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

