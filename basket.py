from operator import index

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
            basket.append((len(basket), obj))


def delete_from_basket(item):
    for i, obj in enumerate(basket):
        if i == int(item):
            basket.remove(obj)


def delete_all_from_basket():
    basket.clear()


def calculate_total():
    total = 0.00
    for obj in basket:
        total = total + obj[1]['attributes']['cost']
    return total

def save_to_newarray(oldarray, newarray):
    for each in oldarray:
        newarray.append(each)