from django.shortcuts import redirect, render
from django.http import FileResponse, HttpResponse
from django.contrib import messages
from .models import Contacts
from .models import Studies
from comments.models import Publish
from comments.models import Comments
from comments.forms import DocumentForm
from django.core.paginator import Paginator
from django.db.models import Q  # لاستعمال البحث المتقدم
import os
from django.conf import settings

def serve_pdf(request, filename):
    # تحديد مسار الملف داخل MEDIA_ROOT
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # التحقق من وجود الملف
    if not os.path.exists(file_path):
        return HttpResponse("الملف غير موجود", status=404)

    # الحصول على نوع العملية من طلب GET (تحميل أو عرض)
    action = request.GET.get('action', 'download')  # القيمة الافتراضية هي "download"

    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()

        response = HttpResponse(file_content, content_type='application/pdf')

        if action == 'view':
            response['Content-Disposition'] = f'inline; filename="{filename}"'
        else:
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
    except Exception as e:
        return HttpResponse(f"حدث خطأ أثناء معالجة الملف: {str(e)}", status=500)

# إنشاء الفيوز باستخدام الدالة العامة
def download_or_view_file(request):
    return serve_pdf(request, 'Future Vision for Administrative Reform.pdf')

def download_or_view_patrols(request):
    return serve_pdf(request, 'Osus-2025-03-Issue.pdf')

def view_osus_content(requst):
    return serve_pdf(requst, 'osus-2025-03-issue-contents.pdf')

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def studies(request):
    context = None
    query = request.GET.get('q', '')  # الحصول على الكلمة المفتاحية من الطلب
    data = Studies.objects.all()
    # تصفية البيانات إذا كان هناك كلمة بحث
    if query:
        data = data.filter(
            Q(subject__icontains=query)
        )
    page = Paginator(data,12)
    page_list = request.GET.get('page')
    
    page = page.get_page(page_list)
    context = {
        'page': page,
        'query': query,  # إضافة الكلمة المفتاحية للسياق لعرضها في القالب
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

def information_and_communications_technology_in_Yemen(request):
    return render(request,'pages/information_and_communications_technology_in_Yemen.html')

def implementing_egovernment_in_Yemen(request):
    return render(request,'pages/implementing_e-government_in_Yemen.html')

def future_of_eGovernment_Yemen(request):
    return render(request,'pages/future_of_eGovernment_Yemen.html')

def show_publications(request):
    return render(request,'pages/show_publications.html')

def osus_journals(request):
    return render(request,'pages/osus_journals.html')

def view_infograph(request):
    infographs = [
        {
            "title": "أكثر سبع دول إنتاجاً للأدوية في العام 2024",
            "slug": "The-seven-largest-pharmaceutical-producing-countries-in-2024",
            "image": "imgs/Info-01.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "أكبر عشر دول في احتياطي اليورانيوم",
            "slug":  "Top-ten-countries-with-the-largest-uranium-reserves",
            "image": "imgs/Info-02.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "الوزارات الحكومية والاقتصادات الخمس الكبرى",
            "slug": "Government-ministries-and-the-big-five-economies",
            "image": "imgs/Info-03.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "البطالة في الدول العربية",
            "slug": "Unemployment-in-Arab-countries",
            "image": "imgs/Info-04.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "كيف يؤثر التعليم على الاقتصاد",
            "slug": "How-education-affects-the-economy",
            "image": "imgs/Info-05.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "مساهمة القطاع الخاص في الناتج المحلي الإجمالي 2023",
            "slug": "Private-sector-contribution-to-GDP-2023",
            "image": "imgs/Info-06.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "ملوك القطن...أكبر عشر دول منتجة للقطن في العالم 2023",
            "slug": "Cotton-kings-2023",
            "image": "imgs/Info-07.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "أكثر عشر دول تصديرًا للمهاجرين في 2023",
            "slug":"Top-10-migrant-exporting-countries-in-2023",
            "image": "imgs/Info-08.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "الضرائب والشركات",
            "slug": "Taxes-and-companies",
            "image": "imgs/Info-09.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "التعليم العالي في العالم العربي",
            "slug": "higher-education-in-the-Arab-World",
            "image": "imgs/Info-10.png",
            "date": "13 مارس 2025",
        },
    ]

    return render(request, 'pages/infographs.html', {'infographs': infographs})

def infograph_detail(request, slug):
    # بيانات ثابتة للكروت
    data = {
        "The-seven-largest-pharmaceutical-producing-countries-in-2024": {
            'title': 'أكثر سبع دول إنتاجاً للأدوية في العام 2024',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-01.png',
        },
        "Top-ten-countries-with-the-largest-uranium-reserves": {
            'title': 'أكبر عشر دول في احتياطي اليورانيوم',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-02.png',
        },
        "Government-ministries-and-the-big-five-economies": {
            'title': 'الوزارات الحكومية والاقتصادات الخمس الكبرى',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-03.png',
        },
         "Unemployment-in-Arab-countries": {
            'title': 'البطالة في الدول العربية',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-04.png',
        },
         "How-education-affects-the-economy": {
            'title': 'كيف يؤثر التعليم على الاقتصاد',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-05.png',
        },
        "Private-sector-contribution-to-GDP-2023": {
            'title': 'مساهمة القطاع الخاص في الناتج المحلي الإجمالي 2023',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-06.png',
        },
        "Cotton-kings-2023": {
            'title': 'ملوك القطن...أكبر عشر دول منتجة للقطن في العالم 2023',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-07.png',
        },
        "Top-10-migrant-exporting-countries-in-2023": {
            'title': 'أكثر عشر دول تصديرًا للمهاجرين في 2023',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-08.png',
        },
        "Taxes-and-companies": {
            'title': 'الضرائب والشركات',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-09.png',
        },
        "higher-education-in-the-Arab-World": {
            'title': 'التعليم العالي في العالم العربي',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-10.png',
        },
    }

    detail = data.get(slug)
    if not detail:
        # يمكنك هنا إعادة توجيه إلى صفحة 404 أو عرض رسالة
        return render(request, 'pages/404.html')

    return render(request, 'pages/infograph_detail.html', {'detail': detail})

    
def error_404(request,exception):
    return render(request,'pages/404_error.html')


   

