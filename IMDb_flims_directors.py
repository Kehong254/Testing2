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

if __name__ == '__main__':
    app.run()

#Error test
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
        error_message = "Database connection error: {}".format(str(e))
        return render_template('error.html', error_message=error_message)

@app.route('/films_details/<Movie_Title>')
def films_details(Movie_Title):
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from films f join directors d on f.Director_ID = d.ID where f.Movie_Title = ?", (Movie_Title,))
        films = cur.fetchall()
        conn.close()
        if not films:
            error_message = "No films found with title: {}".format(Movie_Title)
            return render_template('error.html', error_message=error_message)
        return render_template('films_details.html', films=films)
    except sqlite3.Error as e:
        error_message = "Database query error: {}".format(str(e))
        return render_template('error.html', error_message=error_message)

@app.errorhandler(404)
def page_not_found(e):
    error_message = "Page not found: {}".format(request.url)
    return render_template('error.html', error_message=error_message), 404




