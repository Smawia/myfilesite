from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('all_posts',views.all_posts,name='all_posts'),
    path('<int:post_id>',views.accepting,name='accepting')
]