from django.conf.urls import url
from . import views

urlpatterns = [
    # ------------------------------------------
    # User Login
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

    url(r'user/update_friends$', views.update_friends, name='update_friends'),

    # ----------------------------------------------
    # Update Preferences
    # ----------------------------------------------
    # Input:
    # {USER_TOKEN, [PREFERENCES]}
    # Output: { status: 301/302/303}
    # 301 : successfully updated the preferences
    # 302 : incorrect user_token
    # 303 : something wrong with the database, try again/incorrect sub-keys in the preference key
    # PREFERENCES : {LIST_OF_PRIMARY_CUISINES:[STRINGS],
    #                PRICE_RANGE : INTEGER,
    #                LIST_OF_FAVOURITE_ITEMS : [STRINGS],
    #                LIST_OF_SECONDARY_CUISINES:[STRINGS],
    #                MINIMUM_RATING : FLOAT
    # }

    url(r'user/update_preference$', views.update_preference, name='update_preference'),

    # ----------------------------------------------
    # Update Reviews
    # ----------------------------------------------
    # Input:
    # {USER_TOKEN, [REVIEWS]}
    # Output: { status: 401/402/403}
    # 401 : successfully updated the reviews
    # 402 : incorrect user_token
    # 403 : something wrong with the database, try again/incorrect sub-keys in the reviews key
    # REVIEWS : { RESTAURANT_ID (you get it from the event creation API),
    #                OVERALL_RESTAURANT_RATING : 1,2 or 3 (like, dislike or neutral),
    #                OVERALL_RESTAURANT_REVIEW : STRING,
    #                ITEMS : (list of items)[
    #                      { ITEM_NAME : STRING,
    #                      ITEM_RATING : 1,2 or 3 (like, dislike or neutral),
    #                      ITEM_REVIEW : STRING},
    #
    #                      { ITEM_NAME : STRING,
    #                      ITEM_RATING : 1,2 or 3 (like, dislike or neutral),
    #                      ITEM_REVIEW : STRING} ...
    #                ]
    # }
    url(r'user/update_reviews$', views.update_reviews, name='update_reviews'),

    # ----------------------------------------------
    # get cuisines
    # ----------------------------------------------
    # Input:
    # {USER_TOKEN}
    # Output: { STATUS: 501/502 (success/ incorrect user token),
    #  LIST_OF_CUISINES : [list of cuisines]
    # }

    url(r'restaurant/get_cuisines', views.get_cuisines, name='ger_cuisines'),

]
