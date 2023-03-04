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
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # get results from films
        cur.execute("select * from films")
        rows = cur.fetchall()
        conn.close()
        return render_template('films.html', rows=rows)
    except sqlite3.Error as e:
        return f"An error occurred: {e}"

@app.route('/directors')
def directors():
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # get results from directors
        cur.execute("select * from directors")
        rows = cur.fetchall()
        conn.close()
        return render_template('directors.html', rows=rows)
    except sqlite3.Error as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run()



