from flask import Flask, render_template, request, redirect
from items import data
from basket import basket, basket_message, add_to_basket, delete_from_basket

app = Flask(__name__)


@app.route('/')
def display_page():
    message = basket_message()
    return render_template('index.html', items=data, basket=basket, message=message)

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
