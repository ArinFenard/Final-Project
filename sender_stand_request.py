import requests

import configuration as conf

import data


#   Creating a user

def post_new_order(user_body):
    return requests.post(conf.URL_BASE + conf.ORDER_PATH,
                         json=user_body)


def get_order_track_details(order_number: int):
    return requests.get(conf.URL_BASE + conf.TRACK_ORDER_PATH + str(order_number))


"""
def get_new_user_token(user_body: dict):
    user = data.user_body.copy()

    user["firstName"] = user_body.get("firstName")

    user["phone"] = user_body.get("phone")

    user["address"] = user_body.get("address")

    response = post_new_user(data.user_body)

    return response.json().get("authToken")


def post_new_client_kit(auth_token: str, kit_body: dict):
    header = data.headers.copy()

    header["Authorization"] += auth_token

    return requests.post(conf.URL_BASE + conf.CREATE_KIT_PATH,

                         json=kit_body,

                         headers=header)

"""
