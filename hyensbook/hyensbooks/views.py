from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def play(request):
    return render(request,'play.html')