from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from comments.models import Publish
import re



# Create your views here.
def signin(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['name']
        password = request.POST['pass']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if 'check' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            messages.success(request,'أنت حالياً مسجل دخول')
        else:
            messages.error(request,'هناك خطأ في الاسم أو كلمة السر')
        return redirect('signin')
    
    else:
        return render(request,'accounts/signin.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')

def signup(request):
    fname = None
    lname = None
    address = None
    email = None
    user_name = None
    password = None
    is_added = None

    if request.method == 'POST' and 'signup' in request.POST:
        if 'fname' in request.POST: fname = request.POST['fname']
        else: messages.error(request,'خطأ في الاسم الأول')
        if 'lname' in request.POST: lname = request.POST['lname']
        else: messages.error(request,'خطأ في الاسم الثاني')
        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request,'خطأ في العنوان')
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'خطأ في الإيميل')
        if 'username' in request.POST: user_name = request.POST['username']
        else: messages.error(request,'خطأ في سام المستخدم')
        if 'password' in request.POST: password = request.POST['password']
        else: messages.error(request,'خطأ في كلمة السر')

         # check the variables are not null
        if fname and lname and address and email and user_name and password:
            # check if the user is exsits
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'اسم المستخدم موجود سابقاً')
            else:
                # check if the email is exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'الإيميل موجود سابقاً')
                else:

                    patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                    if re.match(patt,email):
                        # add user
                        user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=user_name,password=password)
                        user.save()

                        # add user profile
                        user_profile = UserProfile(user=user,address=address)
                        user_profile.save()
                        auth.login(request, user)
                        # sucess messages
                        messages.success(request,'تم تسجيل العضوية بنجاح')
                        fname = ''
                        lname = ''
                        address = ''
                        email = ''
                        user_name = ''
                        password = ''
                        is_added = True
                    else:
                        messages.error(request,'هناك خطأ في الإيميل')
        else:
            messages.error(request,'تحقق من وجود حقول فارغة')

        return render(request,'accounts/signup.html',{
            'fname':fname,
            'lname':lname,
            'address':address,
            'email':email,
            'user_name':user_name,
            'password':password,
            'is_added':is_added,
        })
    else:
        return render(request,'accounts/signup.html')

def profile(request):
    return render(request,'accounts/profile.html')



def all_posts(request):
    # is_super = False
    # user = User.objects.all().filter(is_superuser = is_super)
    context = {
        'posts': Publish.objects.all().filter(is_allowed = False)
    }
    return render(request,'accounts/posts.html',context)

def accepting(request,post_id): 
    is_allow = False
    # user = User.objects.get(id=user_id)
    publish = Publish.objects.all().get(id = post_id,is_allowed = False)
    publish.is_allowed = True   
    publish.save()
    is_allow = True
    context = {
        'posts': Publish.objects.all().filter(is_allowed = False),
        'allow': is_allow
    }
    return render(request,'accounts/posts.html',context)