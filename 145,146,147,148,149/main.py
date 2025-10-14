import requests
from bs4 import BeautifulSoup
url ="https://divar.ir/s/mashhad?q=دوچرخه"

headers = {'User-agent':'Mozilla/5.0'}

response = requests.get(url,headers=headers)

with open('divar.html','w',encoding="utf-8") as f:
    f.write(response.text)
print("فایل HTMLبا موفقیت ذخیره شد")