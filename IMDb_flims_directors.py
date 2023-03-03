import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'IMDb_films_directors.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/films')
def films():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from films
    cur.execute("select * from films")
    rows = cur.fetchall()
    conn.close()
    return render_template('films.html', rows=rows)

@app.route('/directors')
def directors():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from directors
    cur.execute("select * from directors")
    rows = cur.fetchall()
    conn.close()
    return render_template('directors.html', rows=rows)




