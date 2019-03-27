import psycopg2


def insert(todo):
    from datetime import datetime
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    now = datetime.now().strftime("%m/%d/%y")
    print(now)
    cur.execute(f"INSERT INTO todos (completed, todo_date, todo_text) VALUES ('N', '{now}', '{todo}');")
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
    cur.execute("CREATE TABLE todos (id bigserial PRIMARY KEY, completed varchar(1) DEFAULT 'N', todo_date date DEFAULT CURRENT_DATE, todo_text text NOT NULL);")
    conn.commit()
    cur.close()
    conn.close()


# Make the changes to the database persistent
# conn.commit()
#
# # Close communication with the database
# cur.close()
# conn.close()
