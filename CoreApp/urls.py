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
    # {FACEBOOK_ID, EMAIL_ID, USER_NAME, GENDER}
    # Output: { status: 101/102/103, user_token: }
    #    Status code 101 : New User.
    #    Status code 102 : Existing User
    #    Status code 103 : Bad Request / Missing Data

    url(r'user/test_login$', views.test_login_user, name='test_login_user'),

    # ------------------------------------------
    # Update Friends List
    # ------------------------------------------
    # Input:
    # {USER_TOKEN, [LIST_OF_FRIENDS]}
    # Output: { status: 101/102/103, user_token: }

    url(r'user/update_friends$', views.update_friends, name='update_friends')

]
