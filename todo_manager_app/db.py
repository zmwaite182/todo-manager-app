import psycopg2

from flask import current_app, g

def connect():
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()

def insert(todo):
    conn = psycopg2.connect(dbname="todos")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO todos (text) VALUES ('{todo}');")
    conn.commit()
    cur.close()
    conn.close()



# Query the database and obtain data as Python objects
# conn = psycopg2.connect(dbname="todos")
# cur = conn.cursor()
# cur.execute("SELECT * FROM todos;")
# thing = cur.fetchone()
# #print(thing)
# things = cur.fetchall()
# print(things)

# # Make the changes to the database persistent
# conn.commit()
#
# # Close communication with the database
# cur.close()
# conn.close()
