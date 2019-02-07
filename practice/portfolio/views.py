from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
  portfolios = Portfolio.objects.all()
  return render(request, 'portfolio.html', {'portfolios': portfolios})

def newportfolio(request): #new.html을 띄워주는 함수
  return render(request, 'newportfolio.html')

def make(request):
    portfolio = Portfolio()
    portfolio.title = request.POST.get('title', '')
    portfolio.description = request.POST.get('description', '')
    portfolio.image = request.POST.get('portfolio.image.url', '')
    portfolio.save()
    return render(request, 'portfolio.html')

  