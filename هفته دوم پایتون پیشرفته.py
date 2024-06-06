import requests
import json 
from bs4 import BeautifulSoup
url = "https://sahmeto.com/crypto-sitmap.xml"
response = requests.get(url)
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content,'xml')
    coins_data = []
    for item in soup.find_all('loc'):
        coin_url = item.text 
        coin_response = requests.get(coin_url)
        if coin_response.status_code == 200:
            coin_content = coin_response.content
            coin_soup = BeautifulSoup(coin_content,'html.parser')
            coin_name = coin_soup.find('h1').text
            coin_data = {"name":coin_name,"url":coin_url,}
            coins_data.append(coin_data)
            coins_json = json.dumps(coins_data,indent=4)