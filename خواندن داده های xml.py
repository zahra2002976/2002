import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
url = "https://sahmeto.com/cypto_sitemap.xml"

response = requests.get(url)

if response.status_code == 200:

    xml_data = response.content
    json_data = bf.data(fromstring(xml_data))

    print(json_data)
else:
    print("Failed to fetch XML data from the URL.")
