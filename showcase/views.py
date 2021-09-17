from django.shortcuts import render
import requests

def index(req):
    r = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=440&count=3\r\n")
    
    data = r.json()
    moar_data =data['appnews']
    even_moar_data = moar_data['newsitems']
    return render(req, 'index.html', {
        'steam_news': even_moar_data
    })