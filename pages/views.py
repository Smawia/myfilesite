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

def download_or_view_second_ossus(request):
    return serve_pdf(request, 'Second-Osus-2025-06-Issue.pdf')

def view_osus_content(requst):
    return serve_pdf(requst, 'osus-2025-03-issue-contents.pdf')
def view_osus_second_content(requst):
    return serve_pdf(requst, 'osus-2025-06-issue-contents.pdf')

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def studies(request):
    query = request.GET.get('q', '')  # كلمة البحث
    db_results = Studies.objects.all()

    if query:
        db_results = db_results.filter(Q(subject__icontains=query))

    # تحويل نتائج DB إلى قائمة مع توحيد الحقول
    combined_results = [
        {
            'subject': item.subject,
            'url': item.url,
            'image': item.image,  # ImageField من DB
            'publish_date': item.publish_date,
            'from_db': True
        }
        for item in db_results
    ]
    # القوائم الثابتة
    issue_one = [
        {'subject': 'اقتصاد السوق الاجتماعي', 'url': 'SocialMarketEconomy', 'image': 'Journal-01.jpg', 'date': '20 مارس  2025', 'from_db': False},
        {'subject': 'النهضة الزراعية في اليمن', 'url': 'AgriculturalRenaissanceInYemen', 'image': 'Journal-02.jpg', 'date': '20 مارس  2025', 'from_db': False},
        {'subject': 'النظام التعليمي في اليمن', 'url': 'EducationalSystemInYemen', 'image': 'Journal-03.jpg', 'date': '20 مارس  2025', 'from_db': False},
        {'subject': 'القضاء في اليمن', 'url': 'JudiciaryInYemen', 'image': 'Journal-04.jpg', 'date': '20 مارس  2025', 'from_db': False},
        {'subject':'الوظائف في اليمن', 'url': 'JobsInYemen', 'image': 'Journal-05.jpg', 'date': '20 مارس  2025', 'from_db': ' False'},
        {'subject': 'النظافة وإدارة النفايات الصلبة', 'url': 'HygieneAndSolidWasteManagement', 'image': 'Journal-06.jpg', 'date': '20 مارس  2025', 'from_db': False},
    ]

    issue_two = [
        {'subject': 'ظاهرة التسول في اليمن', 'url': 'BeggingPhenomenonInYemen', 'image': 'Journal-7.jpg', 'date': '15 يونيو  2025', 'from_db': False},
        {'subject': 'الإدارة المحلية في اليمن', 'url': 'LocalGovernanceInYemen', 'image': 'Journal-8.png', 'date': '15 يونيو  2025', 'from_db': False},   
        {'subject': 'فاعلية المنظومة العدلية والرقابية في اليمن', 'url': 'EffectivenessOfTheJudicialAndOversightSystemInYemen', 'image': 'Journal-9.jpg', 'date': '15 يونيو  2025', 'from_db': False},
        {'subject': 'التأمين الصحي الاجتماعي في اليمن', 'url': 'SocialHealthInsuranceInYemen', 'image': 'Journal-10.jpg', 'date': '15 يونيو  2025', 'from_db': False},   
    ]

    # إضافة القوائم الثابتة بعد البحث فيها
    if query:
        for item in issue_one + issue_two:
            if not query or query in item['subject']:
                combined_results.append({
                    'subject': item['subject'],
                    'url': item['url'],
                    'image': item['image'],  # مسار داخل static
                    'publish_date': item['date']
                })

    # Pagination
    page_number = request.GET.get('page')
    paginator = Paginator(combined_results, 12)
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/studies.html', {'page': page_obj, 'query': query})

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
            "title": "أهم المهارات الوظيفية في 2025",
            "slug": "The_Most_Important_Job_Skills_In_2025",
            "image": "imgs/thinking.jpg",
            "date": "25 أغسطس 2025",
        },
        {
            "title": "الممكلة المتحدة...إصلاح الخدمة المدنية 1979 - 1997",
            "slug": "United-Kingdom-Civil-Service-Reform-1979-1997",
            "image": "imgs/united kingdom.jpg",
            "date": "20 أغسطس 2025",
        },
        {
            "title": "هولندا...من شتاء الجوع إلى الزارعة عالية التقنية",
            "slug": "Netherlands-from-hunger-winter-to-high-tech-agriculture",
            "image": "imgs/netherland.jpg",
            "date": "22 أغسطس 2025",
        },
        {
            "title": "نيوزيلندا من العجز إلى الفائض",
            "slug": "NewZealand-from-deficit-to-surplus",
            "image": "imgs/newzealand.png",
            "date": "16 أغسطس 2025",
        },
        {
            "title": "كندا 1494-1498...المراجعة البرنامجية التي أطفأت العجز",
            "slug": "Canada-the-programmatic-review-that-extinguished-the-deficit",
            "image": "imgs/canada.png",
            "date": "13 أغسطس 2025",
        },
        {
            "title": "الإصلاح الحكومي في اليابان",
            "slug": "Government-reform-in-Japan",
            "image": "imgs/japan.png",
            "date": "10 أغسطس 2025",
        },
        {
            "title": "أكبر البنوك والشركات المصرفية القابضة في العالم 2025",
            "slug": "largest-banks-and-banking-holding-companies-in-2025",
            "image": "imgs/bank.png",
            "date": "3 أغسطس 2025",
        },
        {
            "title": "الشركات الأكثر قيمة في العالم 2025",
            "slug": "worlds-most-valuable-companies-2025",
            "image": "imgs/company.png",
            "date": "3 أغسطس 2025",
        },
        {
            "title": "أكبر الشركات في العالم من حيث عدد العاملين",
            "slug": "largest-companies-in-the-world-by-number-of-employees",
            "image": "imgs/employees.png",
            "date": "3 أغسطس 2025",
        },
        {
            "title": "الثروات الطبيعية وحدها لا تكفي",
            "slug": "natural-resources-alone-are-not-enough",
            "image": "imgs/wealth_five.png",
            "date": "27 يوليو 2025",
        },
        {
            "title": "الثروات لصالح الشعوب",
            "slug": "wealth-for-the-benefit-of-the-people",
            "image": "imgs/wealth_four.png",
            "date": "26 يوليو 2025",
        },
        {
            "title": "ثروات طبيعية معدودة...ودول في الصدرارة",
            "slug": "limited-natural-resources-and-leading-countries",
            "image": "imgs/wealth_three.png",
            "date": "24 يوليو 2025",
        },
        {
            "title": "ثروات طبيعية وفيرة...واقتصادات هشة",
            "slug": "natural-resources-and-fragile-economies",
            "image": "imgs/wealth_two.png",
            "date": "22 يوليو 2025",
        },
        {
            "title": "هل تعني الثروات الطبيعية اقتصادًا قويًا؟",
            "slug": "natural-resources-and-economy",
            "image": "imgs/wealth_one.png",
            "date": "20 يوليو 2025",
        },
        {
            "title": "دول هزمت العطش - سنغافورة",
            "slug": "Countries-that-defeated-thirst-Singabore",
            "image": "imgs/singabor.png",
            "date": "18 يوليو 2025",
        },
        {
            "title": "دول هزمت العطش - الهند",
            "slug": "Countries-that-defeated-thirst-India",
            "image": "imgs/india.png",
            "date": "15 يوليو 2025",
        },
        {
            "title": "دول هزمت العطش - المغرب",
            "slug": "Countries-that-defeated-thirst-Morocco",
            "image": "imgs/morocco.png",
            "date": "11 يوليو 2025",
        },
        {
            "title": "دول هزمت العطش - الأردن",
            "slug": "Countries-that-defeated-thirst-Jordan",
            "image": "imgs/jordan.png",
            "date": "7 يوليو 2025",
        },
        {
            "title": "دول هزمت العطش - أستراليا",
            "slug": "Countries-that-defeated-thirst-Australia",
            "image": "imgs/australia.png",
            "date": "2 يوليو 2025",
        },
        {
            "title": "أكثر عشر دول تصديرًا للمهاجرين في 2023",
            "slug":"Top-10-migrant-exporting-countries-in-2023",
            "image": "imgs/Info-08.png",
            "date": "30 أبريل 2025",
        },
        {
            "title": "أكبر عشر دول عربية إصدارًا وتلقيًا لتحويلات المهاجرين 2024",
            "slug": "The-top-ten-countries-in-remittance-outflows-and-inflows-by-migrants-2024",
            "image": "imgs/Info-20.png",
            "date": "29 أبريل 2025",
        },
        {
            "title": "المياه والدول العربية",
            "slug": "water-and-Arab-countries",
            "image": "imgs/Info-19.png",
            "date": "27 أبريل 2025",
        },
        {
            "title": "أكثر عشر دول في كثافة الأطباء",
            "slug": "top-ten-countries-with-the-most-doctors",
            "image": "imgs/Info-18.png",
            "date": "23 أبريل 2025",
        },
        {
            "title": "أكثر عشر دول في كثافة المعلّمين",
            "slug": "top-ten-countries-with-the-highest-teacher-density",
            "image": "imgs/Info-17.png",
            "date": "20 أبريل 2025",
        },
        {
            "title": "الجيوش الأكبر",
            "slug": "the-largest-armies",
            "image": "imgs/Info-16.png",
            "date": "19 أبريل 2025",
        },
        {
            "title": "هجرة العقول العربية",
            "slug": "the-brain-drain-of-the-Arab-world",
            "image": "imgs/Info-15.png",
            "date": "17 أبريل 2025",
        },
        {
            "title": "أكبر أنظمة رعاية صحية",
            "slug": "largest-healthcare-systems",
            "image": "imgs/Info-14.png",
            "date": "9 أبريل 2025",
        },
        {
            "title": "أكبر عشر أنظمة رعاية اجتماعية",
            "slug": "top-ten-Social-care-Systems",
            "image": "imgs/Info-13.png",
            "date": "7 أبريل 2025",
        },
        {
            "title": "انتشار الأوبئة",
            "slug": "the-spread-of-epidemics",
            "image": "imgs/Info-12.png",
            "date": "3 أبريل 2025",
        },
        {
            "title": "القطاع الصحي في اليمن",
            "slug": "health-care-in-yemen",
            "image": "imgs/Info-11.png",
            "date": "29 مارس 2025",
        },
        {
            "title": "التعليم العالي في العالم العربي",
            "slug": "higher-education-in-the-Arab-World",
            "image": "imgs/Info-10.png",
            "date": "27 مارس 2025",
        },
        {
            "title": "الضرائب والشركات",
            "slug": "Taxes-and-companies",
            "image": "imgs/Info-09.png",
            "date": "25 مارس 2025",
        },
        {
            "title": "ملوك القطن...أكبر عشر دول منتجة للقطن في العالم 2023",
            "slug": "Cotton-kings-2023",
            "image": "imgs/Info-07.png",
            "date": "23 مارس 2025",
        },
        {
            "title": "مساهمة القطاع الخاص في الناتج المحلي الإجمالي 2023",
            "slug": "Private-sector-contribution-to-GDP-2023",
            "image": "imgs/Info-06.png",
            "date": "21 مارس 2025",
        },
        {
            "title": "كيف يؤثر التعليم على الاقتصاد",
            "slug": "How-education-affects-the-economy",
            "image": "imgs/Info-05.png",
            "date": "19 مارس 2025",
        },
        {
            "title": "البطالة في الدول العربية",
            "slug": "Unemployment-in-Arab-countries",
            "image": "imgs/Info-04.png",
            "date": "17 مارس 2025",
        },
        {
            "title": "الوزارات الحكومية والاقتصادات الخمس الكبرى",
            "slug": "Government-ministries-and-the-big-five-economies",
            "image": "imgs/Info-03.png",
            "date": "15 مارس 2025",
        },
        {
            "title": "أكبر عشر دول في احتياطي اليورانيوم",
            "slug":  "Top-ten-countries-with-the-largest-uranium-reserves",
            "image": "imgs/Info-02.png",
            "date": "13 مارس 2025",
        },
        {
            "title": "أكثر سبع دول إنتاجًا للأدوية في العام 2024",
            "slug": "The-seven-largest-pharmaceutical-producing-countries-in-2024",
            "image": "imgs/Info-01.png",
            "date": "11 مارس 2025",
        },
    ]

    return render(request, 'pages/infographs.html', {'infographs': infographs})

def infograph_detail(request, slug):
    # بيانات ثابتة للكروت
    data = {
        "The-seven-largest-pharmaceutical-producing-countries-in-2024": {
            'title': 'أكثر سبع دول إنتاجًا للأدوية في العام 2024',
            'date': '11 مارس 2025',
            'image': 'imgs/Info-01.png',
        },
        "Top-ten-countries-with-the-largest-uranium-reserves": {
            'title': 'أكبر عشر دول في احتياطي اليورانيوم',
            'date': '13 مارس 2025',
            'image': 'imgs/Info-02.png',
        },
        "Government-ministries-and-the-big-five-economies": {
            'title': 'الوزارات الحكومية والاقتصادات الخمس الكبرى',
            'date': '15 مارس 2025',
            'image': 'imgs/Info-03.png',
        },
         "Unemployment-in-Arab-countries": {
            'title': 'البطالة في الدول العربية',
            'date': '17 مارس 2025',
            'image': 'imgs/Info-04.png',
        },
         "How-education-affects-the-economy": {
            'title': 'كيف يؤثر التعليم على الاقتصاد',
            'date': '19 مارس 2025',
            'image': 'imgs/Info-05.png',
        },
        "Private-sector-contribution-to-GDP-2023": {
            'title': 'مساهمة القطاع الخاص في الناتج المحلي الإجمالي 2023',
            'date': '21 مارس 2025',
            'image': 'imgs/Info-06.png',
        },
        "Cotton-kings-2023": {
            'title': 'ملوك القطن...أكبر عشر دول منتجة للقطن في العالم 2023',
            'date': '23 مارس 2025',
            'image': 'imgs/Info-07.png',
        },
        "Top-10-migrant-exporting-countries-in-2023": {
            'title': 'أكثر عشر دول تصديرًا للمهاجرين في 2023',
            'date': '30 أبريل 2025',
            'image': 'imgs/Info-08.png',
        },
        "Taxes-and-companies": {
            'title': 'الضرائب والشركات',
            'date': '25 مارس 2025',
            'image': 'imgs/Info-09.png',
        },
        "higher-education-in-the-Arab-World": {
            'title': 'التعليم العالي في العالم العربي',
            'date': '27 مارس 2025',
            'image': 'imgs/Info-10.png',
        },
        "health-care-in-yemen": {
            'title': 'القطاع الصحي في اليمن',
            'date': '29 مارس 2025',
            'image': 'imgs/Info-11.png',
        },
        "the-spread-of-epidemics": {
            'title': 'انتشار الأوبئة',
            'date': '3 أبريل 2025',
            'image': 'imgs/Info-12.png',
        },
        "top-ten-Social-care-Systems": {
            'title': 'أكبر عشر أنظمة رعاية اجتماعية',
            'date': '7 أبريل 2025',
            'image': 'imgs/Info-13.png',
        },
        "largest-healthcare-systems": {
            'title': 'أكبر أنظمة رعاية صحية',
            'date': '9 أبريل 2025',
            'image': 'imgs/Info-14.png',
        },
        "the-brain-drain-of-the-Arab-world": {
            'title': 'هجرة العقول العربية',
            'date': '17 أبريل 2025',
            'image': 'imgs/Info-15.png',
        },
        "the-largest-armies": {
            'title': 'الجيوش الأكبر',
            'date': '19 أبريل 2025',
            'image': 'imgs/Info-16.png',
        },
        "top-ten-countries-with-the-highest-teacher-density": {
            'title': 'أكثر عشر دول في كثافة المعلّمين',
            'date': '20 أبريل 2025',
            'image': 'imgs/Info-17.png',
        },
        "top-ten-countries-with-the-most-doctors": {
            'title': 'أكثر عشر دول في كثافة الأطباء',
            'date': '23 أبريل 2025',
            'image': 'imgs/Info-18.png',
        },
        "water-and-Arab-countries": {
            'title': 'المياه والدول العربية',
            'date': '27 أبريل 2025',
            'image': 'imgs/Info-19.png',
        },
        "The-top-ten-countries-in-remittance-outflows-and-inflows-by-migrants-2024": {
            'title': 'أكبر عشر دول عربية إصدارًا وتلقيًا لتحويلات المهاجرين 2024',
            'date': '29 أبريل 2025',
            'image': 'imgs/Info-20.png',
        },
        "Countries-that-defeated-thirst-Australia": {
            'title': 'دول هزمت العطش - أستراليا',
            'date': '2 يوليو 2025',
            'image': 'imgs/australia.png',
        },
        "Countries-that-defeated-thirst-Jordan": {
            'title': 'دول هزمت العطش - الأردن',
            'date': '7 يوليو 2025',
            'image': 'imgs/jordan.png',
        },
        "Countries-that-defeated-thirst-Morocco": {
            'title': 'دول هزمت العطش - المغرب',
            'date': '11 يوليو 2025',
            'image': 'imgs/morocco.png',
        },
        "Countries-that-defeated-thirst-India": {
            'title': 'دول هزمت العطش - الهند',
            'date': '15 يوليو 2025',
            'image': 'imgs/india.png',
        },
        "Countries-that-defeated-thirst-Singabore": {
            'title': 'دول هزمت العطش - سنغافورة',
            'date': '18 يوليو 2025',
            'image': 'imgs/singabor.png',
        },
        "top-ten-Arab-countries-sending-migrant-remittances-2024": {
            'title': 'أكبر عشر دول عربية إصدارًا وتلقيًا لتحويلات المهاجرين 2024',
            'date':'29 أبريل 2025',
            'image': 'imgs/Info-20.png',
        },
        "natural-resources-and-economy": {
            'title': 'هل تعني الثروات الطبيعية اقتصادًا قويًا؟',
            'date': '20 يوليو 2025',
            'image': 'imgs/wealth_one.png',
        },
        "natural-resources-and-fragile-economies": {
            'title': 'ثروات طبيعية وفيرة...واقتصادات هشة',
            'date': '22 يوليو 2025',
            'image': 'imgs/wealth_two.png',
        },
        "limited-natural-resources-and-leading-countries": {
            'title': 'ثروات طبيعية معدودة...ودول في الصدرارة',
            'date': '24 يوليو 2025',
            'image': 'imgs/wealth_three.png',
        },
        "wealth-for-the-benefit-of-the-people": {
            'title': 'الثروات لصالح الشعوب',
            'date': '26 يوليو 2025',
            'image': 'imgs/wealth_four.png',
        },
        "natural-resources-alone-are-not-enough": {
            'title': 'الثروات الطبيعية وحدها لا تكفي',
            'date': '27 يوليو 2025',
            'image': 'imgs/wealth_five.png',
        },
        "largest-banks-and-banking-holding-companies-in-2025": {
            'title': 'أكبر البنوك والشركات المصرفية القابضة في العالم 2025',
            'date': '3 أغسطس 2025',
            'image': 'imgs/bank.png',
        },
        "worlds-most-valuable-companies-2025": {
            'title': 'الشركات الأكثر قيمة في العالم 2025',
            'date': '3 أغسطس 2025',
            'image': 'imgs/company.png',
        },
        "largest-companies-in-the-world-by-number-of-employees": {
            'title': 'أكبر الشركات في العالم من حيث عدد العاملين',
            'date': '3 أغسطس 2025',
            'image': 'imgs/employees.png',
        },
        "Canada-the-programmatic-review-that-extinguished-the-deficit": {
            'title': 'كندا 1494-1498...المراجعة البرنامجية التي أطفأت العجز',
            'date': '13 أغسطس 2025',
            'image': 'imgs/canada.png',
        },
        "Government-reform-in-Japan": {
            'title': 'الإصلاح الحكومي في اليابان',
            'date': '10 أغسطس 2025',
            'image': 'imgs/japan.png',
        },
        "NewZealand-from-deficit-to-surplus": {
            'title': 'نيوزيلندا من العجز إلى الفائض',
            'date': '16 أغسطس 2025',
            'image': 'imgs/newzealand.png',
        },
        "Netherlands-from-hunger-winter-to-high-tech-agriculture": {
            'title': 'هولندا...من شتاء الجوع إلى الزارعة عالية التقنية',
            'date': '22 أغسطس 2025',
            'image': 'imgs/netherland.jpg',
        },
        "United-Kingdom-Civil-Service-Reform-1979-1997": {
            'title': 'الممكلة المتحدة...إصلاح الخدمة المدنية 1979 - 1997',
            'date': '20 أغسطس 2025',
            'image': 'imgs/united kingdom.jpg',
        },
        "The_Most_Important_Job_Skills_In_2025": {
            'title': 'أهم المهارات الوظيفية في 2025',
            'date': '25 أغسطس 2025',
            'image': 'imgs/thinking.jpg',
        },
    }

    detail = data.get(slug)
    if not detail:
        # يمكنك هنا إعادة توجيه إلى صفحة 404 أو عرض رسالة
        return render(request, 'pages/404.html')

    return render(request, 'pages/infograph_detail.html', {'detail': detail})

    
def error_404(request,exception):
    return render(request,'pages/404_error.html')


def journal_studies(request):
    context = None
    issue_one = [
        {'subject': 'اقتصاد السوق الاجتماعي', 'url': 'SocialMarketEconomy', 'image': 'imgs/Journal-01.jpg', 'date': '20 مارس  2025'},
        {'subject': 'النهضة الزراعية في اليمن', 'url': 'AgriculturalRenaissanceInYemen', 'image': 'imgs/Journal-02.jpg', 'date': '20 مارس  2025'},
        {'subject': 'النظام التعليمي في اليمن', 'url': 'EducationalSystemInYemen', 'image': 'imgs/Journal-03.jpg', 'date': '20 مارس  2025'},
        {'subject': 'القضاء في اليمن', 'url': 'JudiciaryInYemen', 'image': 'imgs/Journal-04.jpg', 'date': '20 مارس  2025'},
        {'subject':'الوظائف في اليمن', 'url': 'JobsInYemen', 'image': 'imgs/Journal-05.jpg', 'date': '20 مارس  2025'},
        {'subject': 'النظافة وإدارة النفايات الصلبة', 'url': 'HygieneAndSolidWasteManagement', 'image': 'imgs/Journal-06.jpg', 'date': '20 مارس  2025'},
    ]

    issue_two = [
        {'subject': 'ظاهرة التسول في اليمن', 'url': 'BeggingPhenomenonInYemen', 'image': 'imgs/Journal-7.jpg', 'date': '15 يونيو  2025'},
        {'subject': 'الإدارة المحلية في اليمن', 'url': 'LocalGovernanceInYemen', 'image': 'imgs/Journal-8.png', 'date': '15 يونيو  2025'},   
        {'subject': 'فاعلية المنظومة العدلية والرقابية في اليمن', 'url': 'EffectivenessOfTheJudicialAndOversightSystemInYemen', 'image': 'imgs/Journal-9.jpg', 'date': '15 يونيو  2025'},
        {'subject': 'التأمين الصحي الاجتماعي في اليمن', 'url': 'SocialHealthInsuranceInYemen', 'image': 'imgs/Journal-10.jpg', 'date': '15 يونيو  2025'},   
    ]

    context = {
        'issue_one': issue_one,
        'issue_two': issue_two,
    }
    return render(request,'pages/journal_studies.html',context)

def social_market_economy(request):
        return render(request, 'pages/social_market_economy.html')

def agricultural_renaissance_in_yemen(request):
    return render(request, 'pages/agricultural_renaissance_in_yemen.html')

def judiciary_in_yemen(request):
    return render(request, 'pages/judiciary_in_yemen.html')

def jobs_in_yemen(request):
    return render(request, 'pages/jobs_in_yemen.html')

def hygiene_and_solid_waste_management(request):
    return render(request, 'pages/hygiene_and_solid_waste_management.html')

def educational_system_in_yemen(request):
    return render(request, 'pages/educational_system_in_yemen.html')

def begging_phenomenon_in_yemen(request):
    return render(request, 'pages/begging_phenomenon_in_yemen.html')

def local_governance_in_yemen(request):
    return render(request, 'pages/local_governance_in_yemen.html')

def effectiveness_of_the_judicial_and_oversight_system_in_yemen(request):
    return render(request, 'pages/effectiveness_of_the_judicial_and_oversight_system_in_yemen.html')

def social_health_insurance_in_yemen(request):
    return render(request, 'pages/social_health_insurance_in_yemen.html')