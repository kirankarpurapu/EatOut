from CoreApp.Controllers.DatabaseObjects.userprofile_manage import get_user_id
import json


def get_cuisines(request):
    print("request for cuisines list")
    cuisine_list_response = {}
    request_body = json.loads(request.body.decode("utf-8"))
    if "USER_TOKEN" in request_body:
        user_id = get_user_id(request_body["USER_TOKEN"])
        if user_id == 0:
            print("invalid user token while updating preferences")
            cuisine_list_response["STATUS"] = 502
            return cuisine_list_response
        else:
            cuisines = [
                'American',
                'Chinese',
                'Latin',
                'Italian',
                'Mexican',
                'Cafe/Coffee/Tea',
                'Japanese',
                'Caribbean',
                'Bakery',
                'Spanish',
                'Chicken',
                'Indian',
                'Asian',
                'Delicatessen',
                'Jewish/Kosher',
                'French',
                'Hamburgers',
                'Thai',
                'Donuts',
                'Korean',
                'Mediterranean',
                'Irish',
                'Ice Cream',
                'Sandwiches',
                'Seafood',
                'Middle Eastern',
                'Tex-Mex',
                'Greek',
                'Vietnamese',
                'Vegetarian',
                'Peruvian',
                'Russian',
                'Steak',
                'Eastern European',
                'African',
                'Turkish',
                'Beverages',
                'Soul Food',
                'Continental',
                'Barbecue',
                'Pakistani',
                'Salads',
                'Bangladeshi',
                'German',
                'Fillipino',
                'Creole',
                'Tapas',
                'Polish',
                'Brazilian',
                'Armenian',
                'Hotdogs',
                'Ethiopian',
                'Australian',
                'Moroccan',
                'English',
                'Afghan',
                'Portugese',
                'Egyptian',
                'Indonesian',
                'Cajun',
                'Southwestern',
                'Scandinavian',
                'Chilean',
                'Hawaiian',
                'Polynesian',
                'Czech',
                'Iranian',
                'Breakfast',
            ]
            cuisine_list_response["LIST_OF_CUISINES"] = cuisines
            return cuisine_list_response

    else:
        cuisine_list_response["STATUS"] = 502
        return cuisine_list_response
