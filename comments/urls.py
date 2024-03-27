from django.urls import path
from . import views

urlpatterns = [
    path('publish',views.publish,name='publish'),
    path('criteria',views.criteria,name='criteria'),
    # path('show_posts',views.show_posts,name='show_posts'),
    # path('show_patrols_posts',views.show_patrols_posts,name='show_patrols_posts'),
    # path('show_news_posts',views.show_news_posts,name='show_news_posts')
]