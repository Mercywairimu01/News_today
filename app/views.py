from flask import render_template
from .request import get_news,get_news_articles,get_articles
from app import app
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news =get_news()
    title = 'Home - Welcome to The Best News App'
    return render_template('index.html', title = title,news =news)
@app.route('/articles/<news_id>')
def articles(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles =get_news_articles(news_id)
    return render_template('articles.html',articles =articles)
