from flask import Flask, request, render_template
from scripts_py import py_get_data
from scripts_py import search_online
import os

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html', username=name)


@app.route('/get_item_data', methods=['GET', 'POST'])
def get_item_data():
    if request.method == 'POST':
        item_data = request.form.get("name")
        responses = py_get_data.check_url(item_data)
        return responses
    else:
        return render_template('user.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/search_data', methods=['GET', 'POST'])
def search_data():
    if request.method == 'POST':
        search_value = request.form.get("search_value")
        data = search_online.main(search_online.create_url(search_value, 'Egypt'))
        return data
    else:
        return render_template('search.html')


app.run(
    host='localhost', port=5000,
)
