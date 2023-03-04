# IMDb movie rating app
A python Flask web application for managing data on the IMDb website. The application uses a SQLite database to store ratings for a total of 5000 movies on the IMDb website as well as movie information and director information.

## Installation of Framework
Running this application, you should have Python3 and Flask framework installed on your computer. you can install Flask by running the command below:
pip install flask

## Run web application
Copy those code in your terminal:

cd assignment
export FLASK_APP=IMDb_flims_directors.py
export FLASK_ENV=development
python3 -m flask run
Once the app is running, you can access it by visiting http://localhost:5000 in your web browser.

## The application has two main pages.

Movie listings. This page displays a list of 5000 films, including the title, year, director's name, rating, release date, censor, box office and main genre. You can click on the director's name to see the director's information.
There are over 3000 directors in total, including the director's name, the total number of years the director has been filming, the total box office earned and his highest rating.
You can switch between pages using the hyperlinks provided on the page.

## Files

<p>The files are included in the web application below:</p>
<p>IMDb_flims_director.py: This is main FLASK application file. It define the apps routes and views</p>
<p>IMDb_flims_director.db: This is SQLite database file that stores the bar prodecut and transaction</p>
<p>templates/index.html: This file defines the text information and html code for the main page.</p>
<p>templates/films.html: This file defines the information on the movie page as well as the jump links and html code.</p>
<p>templates/directors.html: This file defines the information and html code for the director's page.</p>
<p>templates/films_details.html: This file defines the information and html code for the movie page.</p>
<p></p>
