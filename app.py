from flask import Flask, request, render_template, redirect
from scripts_py import py_get_data
# from scripts_py import search_online
from scripts_py import db_search

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/home/')
def redirect_home():
    return redirect("/eg-en/", code=302)


@app.route('/<string:country>-<string:lang>/')
@app.route('/<string:country>-<string:lang>/home')
@app.route('/<string:country>-<string:lang>/home/')
def index(country, lang):
    if country and lang:
        return render_template('home.html', country=country, lang=lang)


@app.route('/<string:country>-<string:lang>/user/<string:name>')
def user(name, country, lang):
    return render_template('user.html', username=name, country=country, lang=lang)


@app.route('/<string:country>-<string:lang>/search')
@app.route('/<string:country>-<string:lang>/search/')
def search(country, lang):
    return render_template('search.html', data='', country=country, lang=lang)


@app.route('/<string:country>-<string:lang>/search/<search_value>')
def search_data(search_value, country, lang):
    if search_value:
        data = db_search.db_connection(search_value)
        # data = search_online.main(search_online.create_url(search_value, 'Egypt'))
        return render_template('search.html', data=data, country=country, lang=lang)
    else:
        return render_template('search.html', data='', country=country, lang=lang)


@app.route('/<string:country>-<string:lang>/get_item_data', methods=['GET', 'POST'])
def get_item_data():
    if request.method == 'POST':
        item_data = request.form.get("name")
        responses = py_get_data.check_url(item_data)
        return responses
    else:
        return render_template('user.html')


app.run(debug=True, port=5000)
