from flask import Flask, request, render_template
from py_get_data import check_url

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
        responses = check_url(item_data)
        return responses
    else:
        return render_template('user.html')
