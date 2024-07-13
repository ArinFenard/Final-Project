headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "
}

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
}


def get_order_body(order: dict):
    """ Create order body"""
    current_kit_body = order_body.copy()
    current_kit_body["firstName"] = order.get("firstName")
    current_kit_body["lastName"] = order.get("lastName")
    current_kit_body["address"] = order.get("address")
    current_kit_body["metroStation"] = order.get("metroStation")
    current_kit_body["phone"] = order.get("phone")
    current_kit_body["rentTime"] = order.get("rentTime")
    current_kit_body["comment"] = order.get("comment")
    return current_kit_body
