from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('studies',views.studies,name='studies'),
    path('contact',views.contact,name='contact'),
    path('patrols',views.patrols,name='patrols'),
    path('news',views.news,name='news'),
    path('showDetailStudies',views.showDetailStudies,name='showDetailStudies'),
    path('showDetailPatrols',views.showDetailPatrols,name='showDetailPatrols'),
    path('showDetailNews',views.showDetailNews,name='showDetailNews'),
    path('pushStudyPost',views.pushStudyPost,name='pushStudyPost'),
    path('pushPatrolPost',views.pushPatrolPost,name='pushPatrolPost'),
    path('pushNewsPost',views.pushNewsPost,name='pushNewsPost'),
    path('firstStudyPage',views.firstpage,name='firstpage'),
    path('administrativeReform',views.administrative_reform,name='administrativereform'),
]