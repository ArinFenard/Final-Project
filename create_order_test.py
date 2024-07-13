import data
import sender_stand_request as sender

order = {
    "firstName": "Sergey",
    "lastName": "Mistyukov",
    "address": "Voronezh",
    "metroStation": 4,
    "phone": "+7 999 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-07-13",
    "comment": "More COOKEESS",
}

new_order_data = data.get_order_body(order)

def positive_assertion(order_number):
    kit_response_positive = sender.get_order_track_details(order_number)
    assert kit_response_positive.status_code == 200


def test_track_order():
    new_order = sender.post_new_order(new_order_data).json()["track"]
    positive_assertion(new_order)
