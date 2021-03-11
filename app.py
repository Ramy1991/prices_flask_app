from flask import Flask, request, render_template
from scripts_py import py_get_data
# from scripts_py import search_online
from scripts_py import db_search

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/home/')
def index():
    return render_template('home.html')


@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html', username=name)


@app.route('/search')
@app.route('/search/')
def search():
    return render_template('search.html', data='')


@app.route('/search/<search_value>')
def search_data(search_value):
    if search_value:
        # search_value = request.form.get("search_value")
        data = db_search.db_connection(search_value)
        # data = search_online.main(search_online.create_url(search_value, 'Egypt'))
        return render_template('search.html', data=data)
    else:
        return render_template('search.html', data='')
    # if search_value:
    #     return search_value
    # else:
    #     return "default"


#
@app.route('/get_item_data', methods=['GET', 'POST'])
def get_item_data():
    if request.method == 'POST':
        item_data = request.form.get("name")
        responses = py_get_data.check_url(item_data)
        return responses
    else:
        return render_template('user.html')


# app.run(debug=True, port=5000)
