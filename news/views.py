from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def first_announcement(request):
    return render(request,'news/first_announcement.html')

def news(request):
    return render(request,'news/news.html')
