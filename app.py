from flask import Flask, request, render_template, redirect
from scripts_py import py_get_data
from scripts_py import search_online
from scripts_py import db_search
from scripts_py import country_lang
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


@app.route('/')
@app.route('/home')
@app.route('/home/')
def redirect_home():
    return redirect("/eg-en/", code=302)  # to be edit to redirect for country as per region


@app.route('/<string:country>-<string:lang>/')
@app.route('/<string:country>-<string:lang>/home')
@app.route('/<string:country>-<string:lang>/home/')
def index(country, lang):
    if country_lang.validate_country_lang(country, lang):
        return render_template('home.html', country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/user/<string:name>')
def user(name, country, lang):
    if country_lang.validate_country_lang(country, lang):
        return render_template('user.html', username=name, country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/search', methods=['GET', 'POST'])
@app.route('/<string:country>-<string:lang>/search/', methods=['GET', 'POST'])
def search(country, lang):
    if request.method == 'POST' and country_lang.validate_country_lang(country, lang):
        search_val = request.form.get("search_val")
        return redirect(f"/{country}-{lang}/search/{search_val}", code=302)
    elif country_lang.validate_country_lang(country, lang):
        # data = db_search.db_connection('default')
        return render_template('search.html', data='', country=country, lang=lang)
    else:
        return '404'


@app.route('/<string:country>-<string:lang>/search/<search_value>/', defaults={'page_num': 1})
@app.route('/<string:country>-<string:lang>/search/<search_value>/<int:page_num>')
def search_data(search_value, country, lang, page_num):
    if search_value and country_lang.validate_country_lang(country, lang):
        data = db_search.DBSearch(search_value, country, lang, page_num).db_connection()
        pages_count = data[1]
        items = data[0]
        return render_template('search.html', data=items, search_val=search_value, country=country, lang=lang,
                               pages_count=pages_count, page_num=page_num)
    elif country_lang.validate_country_lang(country, lang):
        return render_template('search.html', data='', country=country, lang=lang)
    else:
        return '404'


@app.route('/get_item_data', methods=['GET', 'POST'])
def get_item_data():
    if request.method == 'POST':
        item_data = request.form.get("name")
        responses = py_get_data.check_url(item_data)
        return responses
    else:
        return render_template('user.html')


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(debug=True, port=5000)
