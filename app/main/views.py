from flask import render_template,request,redirect,url_for
from ..request import get_news,get_articles
from . import main
from ..models import News,Articles



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    articles =get_articles()
    
    news =get_news()
    title = 'Home - Welcome to The Best News App'
    return render_template('index.html', title = title,news =news,articles=articles)
