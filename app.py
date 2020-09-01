from flask import Flask, render_template, request, redirect
from items import data
from basket import basket, basket_message, add_to_basket, delete_from_basket, delete_all_from_basket, calculate_total,\
    save_to_newarray


app = Flask(__name__)

@app.route('/')
def display_page():
    total = calculate_total()
    message = basket_message()
    return render_template('index.html', items=data, basket=basket, message=message, total=total)


@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['id']
    add_to_basket(item)
    return redirect("/")


@app.route('/delete', methods=['POST'])
def delete_item():
    item = request.form['index']
    delete_from_basket(item)
    return redirect("/")


@app.route('/clear', methods=['POST'])
def clear_basket():
    delete_all_from_basket()
    return redirect("/")

@app.route('/checkout', methods=['post'])
def checkout():
    total = calculate_total()
    bought = []
    save_to_newarray(basket, bought)
    delete_all_from_basket()
    return render_template('reciept.html', total=total, basket=bought, items=data)
