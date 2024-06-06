from  bs4  import BeautifulSoup

import pandas 

url = "https://catalog.data.gov/dataset"

rssponse = requests.get(url)

soup = Beautifulsoup (rssponse.text)
    