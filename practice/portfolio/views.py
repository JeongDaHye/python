from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
  portfolios = Portfolio.objects.all()
  return render(request, 'portfolio.html', {'portfolios': portfolios})

def newportfolio(request): #newportfolio.html을 띄워주는 함수
  return render(request, 'newportfolio.html')

  