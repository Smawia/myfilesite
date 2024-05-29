from django.urls import path
from . import views

urlpatterns = [
    path('news',views.news,name='news'),
    path('FirstAnnouncement',views.first_announcement,name='first_announcement'),
]