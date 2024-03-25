from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Comments
from .models import Publish
from .forms import DocumentForm
from django.contrib import messages

# Create your views here.

def publish(request):
    publish = None
    file_up = None
    
    if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            file_up = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():

                if  publish and file_up:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.save()
                    # messages.success(request, 'تم إضافة التعليق بنجاح')
                    
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'comments/publish.html')
        
    else:
        return render(request,'comments/publish.html')
    
def criteria(request):
    return render(request, 'comments/criteria.html')

def show_posts(request):
    context = None
    if request.user.is_authenticated:
        study_type = 'studies'
        context = {
        'posts': Publish.objects.all().filter(is_allowed=True,type=study_type)
        }
    return render(request, 'comments/showposts.html',context)

def show_patrols_posts(request):
    context = None
    if request.user.is_authenticated:
        study_type = 'patrols'
        context = {
        'posts': Publish.objects.all().filter(is_allowed=True,type=study_type)
        }
    return render(request, 'comments/showpatrolsposts.html',context)

def show_news_posts(request):
    context = None
    if request.user.is_authenticated:
        study_type = 'news'
        context = {
        'posts': Publish.objects.all().filter(is_allowed=True,type=study_type)
        }
    return render(request, 'comments/shownewsposts.html',context)
     
        
