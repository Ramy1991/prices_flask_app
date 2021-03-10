from flask import Flask, request, render_template
from scripts_py import py_get_data
import requests
from concurrent.futures import ThreadPoolExecutor

# from scripts_py import search_online
# from scripts_py import db_search

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/home/')
def index():
    return render_template('home.html')


@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html', username=name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html', data='')


@app.route('/search/<search_value>')
def search_data(search_value):
    # if search_value:
    #     # search_value = request.form.get("search_value")
    #     data = db_search.db_connection(search_value)
    #     # data = search_online.main(search_online.create_url(search_value, 'Egypt'))
    #     return render_template('search.html', data=data)
    # else:
    return search_value


@app.route('/get_item_data/<url>', methods=['GET', 'POST'])
def get_item_data(url):
    # if request.method == 'POST':
    #     item_data = request.form.get("name")
    #     responses = py_get_data.check_url(item_data)
    #     return responses
    # else:
    #     return render_template('user.html')
    if url:
        link = 'https://egypt.souq.com/eg-en/{}/s/?as=1'.format(url)
        with ThreadPoolExecutor(max_workers=20) as executor:
            request_1 = executor.submit(lambda: requests.get(link))
            html_page = request_1.result().content
            # tree = html.fromstring(html_page)
        # responses = py_get_data.check_url(link)
        return html_page

# app.run(debug=True, port=5000)
