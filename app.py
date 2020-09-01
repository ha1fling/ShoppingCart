from flask import Flask, render_template
from items import data

app = Flask(__name__)


@app.route('/')
def display_index():

    return render_template('index.html', items=data)