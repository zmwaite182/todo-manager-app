from flask import Flask, render_template, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_NAME='flasktodo',
        DB_USER='flasktodo_user'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods = ['GET', 'POST'])
    def index():
        if request.method == 'GET':
            from . import item
            from . import db

            todos = db.retrieve()
            todoList = []

            for each in todos:
                newItem = item.Item(each[1])
                todoList.append(newItem)

            return render_template('index.html', todoList=todoList)
        if request.method == 'POST':
            from . import item
            from . import db

            entry = request.form['text']

            # PLANNING ON CHANGING THE ID VALUES FROM THE HIDDEN INPUT TO BE INTEGERS

            if not isinstance(entry, int):

                newItem = item.Item(entry)

                db.insert(entry)

                todos = db.retrieve()
                todoList = []

                for each in todos:
                    newItem = item.Item(each)
                    todoList.append(newItem)

            else:
                todos = db.retrieve()
                todoList = []

                for each in todos:
                    if each[0] != entry:
                        newItem = item.Item(each[1])
                        todoList.append(newItem)
                    else:
                        newItem = item.Item(each[1])
                        newItem.completed = True
                        todoList.append(newItem)

            return render_template('index.html', todoList=todoList)


    return app
