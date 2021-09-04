from flask import Flask, request, render_template, redirect, session, stream_with_context
from scripts_py import extract_item_data, db_search, product_page, country_lang
from scripts_py import search_online
# from scripts_py import
# from scripts_py import country_lang
from flask_compress import Compress
from threading import Thread
import json
import time
import requests
import re
from fake_useragent import UserAgent

app = Flask(__name__)
app.secret_key = '0000'
Compress(app)


@app.route('/')
@app.route('/home')
@app.route('/home/')
def redirect_home():
    return redirect("/eg-en/", code=302)  # to be edit to redirect for country as per region


# home
@app.route('/<string:country>-<string:lang>/')
@app.route('/<string:country>-<string:lang>/home')
@app.route('/<string:country>-<string:lang>/home/')
def index(country, lang):
    if country_lang.validate_country_lang(country, lang):
        return render_template('home.html', country=country, lang=lang)
    else:
        return '404'


# user page
@app.route('/<string:country>-<string:lang>/user/<string:name>')
def user(name, country, lang):
    if country_lang.validate_country_lang(country, lang):
        return render_template('user.html', username=name, country=country, lang=lang)
    else:
        return '404'


# search page
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


# request to get new items by search value after user search
def user_agent():
    return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 14;)"


def get_new_items(search_val, country, lang):
    header = {
        "User-Agent": user_agent(),
        "Accept": "*/*",
        "Accept-Language": "*/*",
        "Accept-Charset": "*/*",
        "Connection": "keep-alive",
        "Keep-Alive": "300"
    }
    my_data = {'search_val': search_val, 'country': country, 'lang': lang}
    x = requests.post('https://prices-assist.herokuapp.com/search_items_online', data=my_data, headers=header)
    print(x.text)


# search page
@app.route('/<string:country>-<string:lang>/search/<search_value>/', defaults={'page_num': 1})
@app.route('/<string:country>-<string:lang>/search/<search_value>/<int:page_num>')
def search_data(search_value, country, lang, page_num):
    if search_value and country_lang.validate_country_lang(country, lang):
        data = db_search.DBSearch(search_value, country, lang, page_num).db_connection()
        pages_count = data[1]
        items = data[0]
        # request to get new items by search value after user search
        Thread(target=get_new_items, args=(search_value, country, lang)).start()
        ###
        return render_template('search.html', data=json.loads(items), search_val=search_value, country=country,
                               lang=lang, pages_count=pages_count, page_num=page_num)
    elif country_lang.validate_country_lang(country, lang):
        return render_template('search.html', data='', country=country, lang=lang)
    else:
        return '404'


# product_page
@app.route('/<string:country>-<string:lang>/p/<string:uid>')
def product_info(country, lang, uid):
    if country_lang.validate_country_lang(country, lang):
        product_data = product_page.ProductPage(country, lang, uid).db_connection()
        session['data'] = json.loads(product_data)
        if session.get('data').get('item_data'):
            return redirect(f"/{country}-{lang}/p/{session.get('data')['item_data']['item_link']}", code=302)
        else:
            return render_template('product_page.html', data=session['data'], country=country, lang=lang)


@app.route('/<string:country>-<string:lang>/p/<string:cate>/<string:title>/<string:uid>')
def product_p(country, lang, cate, title, uid):
    if country_lang.validate_country_lang(country, lang):
        if session.get('data'):
            item_data = session.get('data')
            session.pop('data', None)
            return render_template('product_page.html', data=item_data, country=country, lang=lang)
        else:
            return redirect('/{}-{}/p/{}'.format(country, lang, uid), code=302)


# search online for items
live_requests = 0


@app.route('/get_item_data', methods=['GET', 'POST'])
def get_item_data():
    global live_requests
    if request.method == 'POST':
        if not live_requests:
            live_requests = 1
        else:
            live_requests += 1
        item_url = request.form.get("name")
        responses = extract_item_data.check_url(item_url)
        live_requests -= 1
        return responses
    else:
        return ''


@app.route('/count_live_requests', methods=['GET', 'POST'])
def count_live_sessions():
    if live_requests:
        def generate():
            yield str(live_requests)
        return app.response_class(stream_with_context(generate()))
    else:
        return 'test'


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(debug=True, port=5000)
