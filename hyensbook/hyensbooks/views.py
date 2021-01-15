from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Article

count=0
def play(request):
    id='bts'
    global count
    count+=1
    return render(request,'play.html',{'name' : id,'cnt' : count})
def play2(request):
    id='bts'
    global count
    count+=1
    result=''
    if count%2==1:
        result='당 첨'
    else:
        result='꽝'
    return render(request,'play2.html',{'name' : id,'cnt' : count,'result':result,'diary':['a','b','c']})
def profile(request):
    id='bts'
    global count
    count+=1
    return render(request,'profile.html',{'name' : id,'cnt' : count})
def newsfeed(request):
    articles = Article.objects.all()
    return render(request,'newsfeed.html',{'articles' : articles})
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail.html', {'feed': article})