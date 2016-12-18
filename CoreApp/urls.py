from django.conf.urls import url
from . import views

urlpatterns = [
    # ------------------------------------------
    # Login urls
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
    # {USER_TOKEN, [LIST_OF_FRIENDS_FACEBOOK_IDS]}
    # Output: { status: 201/202}

    url(r'user/update_friends$', views.update_friends, name='update_friends')

]
