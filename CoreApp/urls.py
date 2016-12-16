from django.conf.urls import url
from . import views

urlpatterns = [

    # views.index is the function to handle this url
    url(r'^$', views.index, name='index'),
    url(r'^page1/$', views.page1, name='page1'),
    url(r'^page1/subpage1', views.sub_page1, name='page1'),
    url(r'^(?P<question_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'post$', views.handle_post, name='handlepost')
]
