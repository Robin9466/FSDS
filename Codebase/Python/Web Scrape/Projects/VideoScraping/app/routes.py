# In app/routes.py

from flask import request, render_template, redirect, url_for
from app import app
from backend import scrape_youtube_data, insert_mysql_data, insert_mongodb_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form.get('video_link')
        if video_link:
            # Scrape YouTube data
            youtube_data = scrape_youtube_data(video_link)

            # Insert data into MySQL
            insert_mysql_data(youtube_data)

            # Insert data into MongoDB
            insert_mongodb_data(youtube_data)

            return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')
