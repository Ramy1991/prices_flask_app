from flask import Flask, request, render_template, redirect
from scripts_py import py_get_data
from scripts_py import search_online
from scripts_py import db_search
from scripts_py import country_lang

app = Flask(__name__)


# validate country and land


@app.route('/')
@app.route('/home')
@app.route('/home/')
def redirect_home():
    return redirect("/eg-en/", code=302)


@app.route('/<string:country>-<string:lang>/')
@app.route('/<string:country>-<string:lang>/home')
@app.route('/<string:country>-<string:lang>/home/')
def index(country, lang):
    if country_lang(country, lang):
        return render_template('home.html', country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/user/<string:name>')
def user(name, country, lang):
    if country_lang(country, lang):
        return render_template('user.html', username=name, country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/search')
@app.route('/<string:country>-<string:lang>/search/')
def search(country, lang):
    if country_lang(country, lang):
        # data = db_search.db_connection('default')
        return render_template('search.html', data='', country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/search/<search_value>')
def search_data(search_value, country, lang):
    if search_value and country_lang(country, lang):
        # data = db_search.db_connection(search_value)
        data = search_online.main(search_online.create_url(search_value, country, lang))
        return render_template('search.html', data=data, country=country, lang=lang)
    elif country_lang(country, lang):
        return render_template('search.html', data='', country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/get_item_data', methods=['GET', 'POST'])
def get_item_data(country, lang):
    if country_lang(country, lang):
        if request.method == 'POST':
            item_data = request.form.get("name")
            responses = py_get_data.check_url(item_data)
            return responses
        else:
            return render_template('user.html')
    else:
        return '404'


app.run(debug=True, port=5000)
