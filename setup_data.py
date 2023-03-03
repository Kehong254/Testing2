import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('IMDb_films_directors.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS IMDb_All_Genres_etf_clean1')
print("table dropped successfully");

# create table
cur.execute('''CREATE TABLE IMDb_All_Genres_etf_clean1
               (Movie_Title TEXT, Year TEXT, Director TEXT, Rating TEXT, Runtime TEXT, Censor TEXT, Total_Gross TEXT, main_genre TEXT)''')

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

        cur.execute('INSERT INTO IMDb_All_Genres_etf_clean1 VALUES (?,?,?,?,?,?,?,?)', (Movie_Title, Year, Director, Rating, Runtime, Censor, Total_Gross, main_genre))
        conn.commit()

print("data parsed successfully")
conn.close()