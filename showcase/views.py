from django.shortcuts import render
import requests, environ
from datetime import datetime

env = environ.Env()
environ.Env.read_env()

def index(req):
    #steam news
    r = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=440&count=5\r\n")
    
    data = r.json()
    moar_data =data['appnews']
    even_moar_data = moar_data['newsitems']
    articles = []
    for article in even_moar_data:
        print(article)
        articles.append(article)
    today = datetime.now()
    print(today)
    #Tech news
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'category=technology&'
        'from='+str(today)+'&'
        'sortBy=popularity&'
        'apiKey='+str(env('NEWS_API_KEY')))

    tech_array = []
    response = requests.get(url)
    reeeesponse = response.json()
    filtered_response = reeeesponse['articles']
    for article in filtered_response:
        tech_array.append(article)
    return render(req, 'index.html', {
        'steam_news': articles,
        'tech_news': tech_array
    })