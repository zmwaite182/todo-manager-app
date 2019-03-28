import psycopg2


def insert(todo):
    from datetime import datetime
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    now = datetime.now().strftime("%m/%d/%y")
    cur.execute(f"INSERT INTO todos (completed, todo_date, todo_text) VALUES (False, '{now}', '{todo}');")
    conn.commit()
    cur.close()
    conn.close()

def retrieve():
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos;")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return todos


def init_db():
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    cur.execute("CREATE TABLE todos (id bigserial PRIMARY KEY, completed boolean NOT NULL, todo_date date NOT NULL, todo_text text NOT NULL);")
    conn.commit()
    cur.close()
    conn.close()

def restart_db():
    from flask import current_app

    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    cur.execute(current_app.open_resource('schema.sql').read().decode('utf8'))
    conn.commit()
    cur.close()
    conn.close()

restart_db()
