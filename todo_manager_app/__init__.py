from flask import Flask, render_template, request
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods = ['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            class Item(object):
                def __init__(self, text):
                    self.completed = False
                    self.time = datetime.now().strftime("%m-%d")
                    self.text = text

            entry = request.form['text']
            instance = Item(entry)
            item = f'{instance.time} | {instance.text}'

            return render_template('index.html', item=item, completed=instance.completed)

    @app.route('/update', methods = ['GET', 'POST'])
    def update(todo):
        return render_template('index.html')

    return app
