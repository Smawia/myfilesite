from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contacts
from .models import Studies
from comments.models import Publish
from comments.models import Comments
from comments.forms import DocumentForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request,'pages/index.html')


def about(request):
    return render(request,'pages/about.html')

def studies(request):
    # typeData = 'studies'
    # Publish.objects.all().filter(type=typeData)
    context = None

    # data = ['نشأة الإدارة وتطورها','الإصلاح الإداري المفهوم والأهداف','منهجية الإصلاح الإداري','ملاحظات على مداخل الإصلاح الإداري','تجربة الولايات المتحدة الأمريكية في الإصلاح الإداري','تجربة سنغافورا في الإصلاح الإداري']

    data = Studies.objects.all()

    page = Paginator(data,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page
    }
    return render(request,'pages/studies.html',context)

def contact(request):
    sugg = None
    email = None
    if request.method == 'POST' and 'sub' in request.POST:
        if 'ta' in request.POST: sugg = request.POST['ta']
        else: messages.error(request,'قم بادخال مقترحك ')
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'قم بادخال إيميلك ')

        if sugg and email:
            contact = Contacts()
            contact.suggestion = sugg
            contact.email = email
            contact.save()
            messages.success(request, 'تم اضافة مقترحك')
            return render(request,'pages/contact.html')
        else:
            messages.error(request, 'تحقق من وجود حقول فارغة')
    return render(request,'pages/contact.html')

def patrols(request):
    typeData = 'patrols'
    context = None

    context = {
        'posts':Publish.objects.all().filter(type=typeData)
    }
    return render(request,'pages/patrols.html',context)


def showDetailStudies(request):
    name = None
    email = None
    comment = None

    if request.method == 'POST' and 'send' in request.POST:
        if 'name' in request.POST: name = request.POST['name']
        else: messages.error(request, 'خطأ في الاسم')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'خطأ في الإيميل')

        if 'comment' in request.POST: comment = request.POST['comment']

        if name and email and comment:
            new_comment = Comments()
            new_comment.name = name
            new_comment.email = email
            new_comment.comment = comment
            new_comment.type = 'studies'
            new_comment.save()
            messages.success(request, 'تم إضافة التعليق بنجاح')
            context = {
                'comments': Comments.objects.all().filter(type='studies')
             }
        else:
            messages.error(request, 'تحقق من وجود حقول فارغة')
        return render(request,'pages/showDetailStudies.html',context)
    else:
        context = {
                'comments': Comments.objects.all().filter(type='studies')
             }
        return render(request,'pages/showDetailStudies.html',context)

def pushStudyPost(request):
    publish = None
    file_up = None
    file_up2 = None
    type = None
    
    if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            file_up2 = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid() and file_up2.is_valid():

                if  publish and file_up and type and file_up2:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.file2 = request.FILES['docfile2']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/pushStudyPost.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/pushStudyPost.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/pushStudyPost.html')
        
    else:
        return render(request,'pages/pushStudyPost.html')
    
def pushPatrolPost(request):
    publish = None
    file_up = None
    file_up2 = None
    type = None
    
    if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            file_up2 = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():

                if  publish and file_up and file_up2 and type:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.file2 = request.FILES['docfile2']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/pushPatrolPost.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/pushPatrolPost.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/pushPatrolPost.html')
        
    else:
        return render(request,'pages/pushPatrolPost.html')
    
def showDetailPatrols(request):
    name = None
    email = None
    comment = None

    if request.method == 'POST' and 'send' in request.POST:
        if 'name' in request.POST: name = request.POST['name']
        else: messages.error(request, 'خطأ في الاسم')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'خطأ في الإيميل')

        if 'comment' in request.POST: comment = request.POST['comment']

        if name and email and comment:
            new_comment = Comments()
            new_comment.name = name
            new_comment.email = email
            new_comment.comment = comment
            new_comment.type = 'patrols'
            new_comment.save()
            messages.success(request, 'تم إضافة التعليق بنجاح')
            context = {
                'comments': Comments.objects.all().filter(type='patrols')
             }
        else:
            messages.error(request, 'تحقق من وجود حقول فارغة')
        return render(request,'pages/showDetailPatrols.html',context)
    else:
        context = {
                'comments': Comments.objects.all().filter(type='patrols')
             }
        return render(request,'pages/showDetailPatrols.html',context)

def showDetailNews(request):
    name = None
    email = None
    comment = None

    if request.method == 'POST' and 'send' in request.POST:
        if 'name' in request.POST: name = request.POST['name']
        else: messages.error(request, 'خطأ في الاسم')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'خطأ في الإيميل')

        if 'comment' in request.POST: comment = request.POST['comment']

        if name and email and comment:
            new_comment = Comments()
            new_comment.name = name
            new_comment.email = email
            new_comment.comment = comment
            new_comment.type = 'news'
            new_comment.save()
            messages.success(request, 'تم إضافة التعليق بنجاح')
            context = {
                'comments': Comments.objects.all().filter(type='news')
             }
        else:
            messages.error(request, 'تحقق من وجود حقول فارغة')
        return render(request,'pages/showDetailNews.html',context)
    else:
        context = {
                'comments': Comments.objects.all().filter(type='news')
             }
        return render(request,'pages/showDetailNews.html',context)
   
def pushNewsPost(request):
    publish = None
    file_up = None
    file_up2 = None
    type = None
    
    if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            file_up2 = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():
                if  publish and file_up and file_up2 and type:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.file2 = request.FILES['docfile2']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/pushNewsPost.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/pushNewsPost.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/pushNewsPost.html')
        
    else:
        return render(request,'pages/pushNewsPost.html')
    
def firstpage(request):
    return render(request,'pages/firstpage.html')

def administrative_reform(request):
    return render(request,'pages/administrative_reform.html')

def reform_methodology(request):
    return render(request,'pages/reform_methodology.html')

def Notes_reform(request):
    return render(request,'pages/Notes_reform.html')

def study_of_US(request):
    return render(request,'pages/studyUS.html')

def studysingapore(request):
    return render(request,'pages/study_singapore.html')

def rwanda_study(request):
    return render(request,'pages/rwanda_study.html')

def china_study(request):
    return render(request,'pages/china_study.html')

def malaysia_study(request):
    return render(request,'pages/malaysia_study.html')

def jor_study(request):
    return render(request,'pages/jor_study.html')

def features_of_administrative_reform_in_yemen(request):
    return render(request,'pages/features_of_administrative_reform_in_yemen.html')

def comprehensive_reform(request):
    return render(request,'pages/comprehensive_reform.html')

def administrative_raw(request):
    return render(request,'pages/administrative_raw.html')

def administrative_reform2(request):
    return render(request,'pages/administrative_reform2.html')

def administrative_law_in_yemen(request):
    return render(request,'pages/administrative_law_in_yemen.html')

def global_management_reform(request):
    return render(request,'pages/global_management_reform.html')

def future_fo_reforming_administrative_law_in_yemen(request):
    return render(request,'pages/future_fo_reforming_administrative_law_in_yemen.html')

def legal_reform(request):
    return render(request,'pages/legal_reform.html')

def evolution_of_public_administration(request):
    return render(request,'pages/evolution_of_public_administration.html')

def stages_of_legislative_reform(request):
    return render(request,'pages/stages_of_legislative_reform.html')

def legislative_reform_in_the_world(request):
    return render(request,'pages/legislative_reform_in_the_world.html')

def legal_reform_in_yemen(request):
    return render(request,'pages/legal_reform_in_yemen.html')

def general_administration_in_yemen(request):
    return render(request,'pages/general_administration_in_yemen.html')

def books(request):
    return render(request,'pages/books.html')

def current_economic_situation(request):
    return render(request,'pages/current_economic_situation.html')

def the_existing_social_situation(request):
    return render(request,'pages/the_existing_social_situation.html')

def the_influence_of_the_bureaucratic_apparatus_on_administrative_reform(request):
    return render(request,'pages/the_influence_of_the_bureaucratic_apparatus_on_administrative_reform.html')

def public_finance_and_economic_construction(request):
    return render(request,'pages/public_finance_and_economic_construction.html')

def financial_reform_in_countries(request):
    return render(request,'pages/financial_reform_in_countries.html')

def financial_reform_in_yemen(request):
    return render(request,'pages/financial_reform_in_yemen.html')

def future_of_financial_reform_in_yemen(request):
    return render(request,'pages/future_of_financial_reform_in_yemen.html')

def the_private_sector_inyemen(request):
    return render(request,'pages/the_private_sector_inyemen.html')

def role_of_the_private_sector_in_world(request):
    return render(request,'pages/role_of_the_private_sector_in_world.html')

def role_of_the_private_sector_in_development_in_yemen(request):
    return render(request,'pages/role_of_the_private_sector_in_development_in_yemen.html')

def future_of_private_sector_in_Yemen(request):
    return render(request,'pages/future_of_private_sector_in_Yemen.html')

def Government(request):
    return render(request,'pages/E-Government.html')

def implementing_egovernment(request):
    return render(request,'pages/implementing_e-government.html')

def global_experiences_in_egovernment(request):
    return render(request,'pages/global_experiences_in_egovernment.html')
    
def error_404(request,exception):
    return render(request,'pages/404_error.html')


   

