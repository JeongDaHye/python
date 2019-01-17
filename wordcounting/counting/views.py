from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import operator
def index(request):
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def result(request):
  text = request.GET['fulltext']
  words = text.split()
  word_dictionary = {}
  for word in words:
    if word in word_dictionary:
      word_dictionary[word] += 1
    else:
      word_dictionary[word] = 1
  sorting = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
  return render(request,'result.html', {'full' : text, 'total' :len(words), 'dictionary' :sorting})  
       