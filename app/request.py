
  
from app import app
import urllib.request,json
from .models import news,articles

News = news.News
Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
news_base_url = app.config["NEWS_API_BASE_URL"]



#Getting General Url
general_url = app.config['GENERAL_URL']

def get_news():
    """
     Function that gets the json response to our url request
    """
    get_news_url =news_base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as source_url:
            get_news_data = source_url.read()
            get_news_response = json.loads(get_news_data)
            # print(get_news_response)
            news_results = None

            if get_news_response['sources']:
                news_results_list = get_news_response['sources']
                news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id =news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url') 
        category = news_item.get('category')
        country = news_item.get('country')
        

        if description:   
            news_object = News(id, name, description, url, category,country)
            news_results.append(news_object)

    return news_results

def get_articles():
    get_all_articles_url = general_url.format(api_key) 
    with urllib.request.urlopen(get_all_articles_url) as url:
        all_articles =url.read()
        articles_response =json.loads(all_articles)      
        # print(articles_response)
        articles_results= None
        
        if articles_response['articles']:
          articles_results_list = articles_response['articles']
          articles_results =process_articles(articles_results_list)
          
    return articles_results 
def process_articles(articles_list):
    '''
    Function that process articles results and transform them to list of objects
    Args:
        articles_list: Dictionary that contain articles 
    Returns:
        articles_results: List of new objects
    '''
    articles_results = []
    for article in articles_list:
        # source = article.get('source.id')
        id =article.get("id")
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        if description:
            article_object = Articles(id, author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object) 

    return articles_results