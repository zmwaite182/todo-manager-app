from flask import Flask, render_template, request

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
            from . import item
            from . import db

            entry = request.form['text']
            newItem = item.Item(entry)

            db.connect()
            db.insert(entry)

            return render_template('index.html', newItem=newItem, completed=newItem.completed)

    @app.route('/update', methods = ['GET', 'POST'])
    def update(todo):
        return render_template('index.html')

    return app
