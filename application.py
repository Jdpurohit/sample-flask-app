from flask import Flask, render_template, request
from models import get_method, create_method

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_method(name, post)

    posts = get_method()
    return render_template('index.html', posts=posts)