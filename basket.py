from items import data
basket = []


def basket_message():
    if len(basket) == 0:
        return "the basket is empty"
    else:
        return "here is your basket"


def add_to_basket(item):
    for obj in data:
        if obj["id"] == int(item):
            basket.append(obj)
            print(basket)
