from django.conf.urls import url
from . import views

urlpatterns = [

    # ------------------------------------------
    # index url
    # ------------------------------------------
    url(r'^$', views.index, name='index'),

    # ------------------------------------------
    # miscellaneous urls
    # ------------------------------------------

    url(r'^page1/$', views.page1, name='page1'),

    url(r'^page1/subpage1', views.sub_page1, name='page1'),

    url(r'^(?P<question_id>[0-9]+)/details/$', views.details, name='details'),

    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    url(r'post$', views.handle_post, name='handle_post'),

    # ------------------------------------------
    # login urls
    # ------------------------------------------

    # Input:
    # 1. [FACEBOOK_ID]
    # Output:
    # 1. Status code :[STATUS] = 1 : successful login
    #    Status code :[STATUS] = 2 : new account needs to be created, pass more details
    #    Status code :[STATUS] = 3 : missing data
    # 2. [USER_TOKEN] : User_Token(String, length = 32)

    url(r'user/test_login$', views.test_login_user, name='test_login_user'),

    # Input:
    # 1. [FACEBOOK_ID]
    # 2. [GENDER]
    # 3. [AGE]
    # 4. [EMAIL_ID]
    # 5. [PROFILE_PIC_URL]
    # 6. [NAME]
    # Output:
    # 1. Status code :[STATUS] = 1 : successful signup
    #    Status code :[STATUS] = 2 : missing data
    #    Status code : [STATUS] = 3 :
    # 2. [USER_TOKEN] : User_Token(String, length = 32)


    url(r'user/signup$', views.signup_user, name='signup_user')

]
