from flask import render_template
from .request import get_news,get_articles
from app import app
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    articles =get_articles()
    
    news =get_news()
    title = 'Home - Welcome to The Best News App'
    return render_template('index.html', title = title,news =news,articles=articles)
# @app.route('/articles')
# def articles():

#     '''
#     View news page function that returns the news details page and its data
#     '''
    
#     return render_template('articles.html',articles =articles)
    
# @app.route('/sports')
# def sports():
#     title = 'sports'
#     articles = get_articles('sports')
#     return render_template('sports.html',articles = articles,title = title)

# @app.route('/business')
# def politics():
#     title ='business'
#     articles = get_articles('business')
#     return render_template('business.html',articles = articles,title = title)

# @app.route('/technology')
# def tech():
#     title = 'technology'
#     articles = get_articles('technology')
#     return render_template('technology.html',articles = articles,title = title)

# @app.route('/entertainment')
# def entertainment():
#     title = 'entertainment'
#     articles = get_articles('entertainment')
#     return render_template('entertainment.html',articles = articles,title = title)

# @app.route('/health')
# def health():
#     title = 'health'
#     articles = get_articles('health')
#     return render_template('health.html',articles = articles,title = title)

