import re
from bs4 import BeautifulSoup
with open('divar.html','r',encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all('div',class_='kt-post-card__description')

for item in items:
    text=item.text
    # print(text)
    match=re.search(r'(\d[\d,]*)\s*تومان',text)
    if match:
        price=match.group(1).replace(',','')
        print(f"{price}")