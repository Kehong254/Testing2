import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('IMDb_films_directors.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS films')
conn.execute('DROP TABLE IF EXISTS directors')
print("table dropped successfully");

# create table
cur.execute('''CREATE TABLE films
               (Movie_Title TEXT, Year TEXT, Director TEXT, Rating TEXT, Runtime TEXT, Censor TEXT, Total_Gross TEXT, main_genre TEXT)''')
cur.execute('''CREATE TABLE directors
               (Director TEXT, Time_span TEXT, Total_Money TEXT, Highest_rating TEXT)''')

# open the file to read it into the database
with open('IMDb_movies_director/IMDb_All_Genres_etf_clean1.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Movie_Title = row[0]
        Year = row[1]
        Director = row[2]
        Rating = row[3]
        Runtime = row[4]
        Censor = row[5]
        Total_Gross = row[6]
        main_genre = row[7]

        cur.execute('INSERT INTO IMDb_All_Genres_etf_clean1 VALUES (?,?,?,?,?,?,?,?)', row)
        conn.commit()

with open('IMDb_movies_director/Director.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Director = row[0]
        Time_span = row[1]
        Total_Money = row[2]
        Highest_rating = row[3]

        cur.execute('INSERT INTO Director VALUES (?,?,?,?)', row)
        conn.commit()

print("data parsed successfully")
conn.close()