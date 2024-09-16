from flask import request, render_template, redirect, url_for
from app import app
from backend.scraper import scrape_youtube_data
from backend.database import insert_mysql_data, insert_mongodb_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form.get('video_link')
        if video_link:
            # Continue with the scraping and database insertion logic

    return render_template('index.html')
