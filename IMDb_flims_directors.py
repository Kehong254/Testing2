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

@app.route('/films_details/<Movie_Title>')
def films_details(Movie_Title):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from films f join directors d on f.Director_ID = d.ID where f.Movie_Title = ?", (Movie_Title,))
    films = cur.fetchall()
    conn.close()
    return render_template('films_details.html', films=films)

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

@app.route('/directors_details/<Director>')
def directors_details(Director):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT d.*, f.* FROM directors d JOIN films f ON d.ID = f.Director_ID WHERE d.Director = ?", (Director,))
    directors = cur.fetchall()
    conn.close()
    return render_template('directors_details.html', directors=directors)


app.run()



