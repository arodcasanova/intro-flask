from flask import Flask, render_template
from functions import get_sports_news_data, get_tech_news_data

my_flask_app = Flask(__name__)

@my_flask_app.route("/")
def render_html_for_home_page():
    return render_template('home.html')

@my_flask_app.route("/sports")
def render_html_for_sports_page():
    sport_news_data = get_sports_news_data()
    return render_template('sports.html', sports_articles=sport_news_data)

@my_flask_app.route("/tech")
def render_html_for_tech_page():
    tech_news_data = get_tech_news_data()
    return render_template('tech.html', tech_articles=tech_news_data)
