from bs4 import BeautifulSoup

with open('divar.html','r',encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all('div',class_='kt-post-card__description')

# friends=['reza','karim','mohamad']
# for i,item in enumerate(friends):
#     print(f"{i+1}.{item}")

for i , item in enumerate(items[:5]):
    print(f"{i+1}. {item.text.strip()}")