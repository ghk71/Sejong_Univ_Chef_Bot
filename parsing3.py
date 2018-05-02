from bs4 import BeautifulSoup
import urllib.request
import json

html = urllib.request.urlopen("http://m.sejong.ac.kr/front/cafeteria.do")
text = html.read().decode("utf8")

soup = BeautifulSoup(text, 'html.parser')

menu = soup.find_all('div',{'class':'th'})
price = soup.find_all('div',{'class':'td price'})

##리스트 menu와 price에 쓰레기값 제거
for n in menu:
    i = menu.index(n)
    menu[i]= n.get_text()
for n in price:
    i = price.index(n)
    price[i]= n.get_text()

##딕셔너리 생성
foodlist={}

for i in range(0,len(menu)):
    foodlist[i+1]=menu[i]+" "+price[i]

print(json.dumps(foodlist,indent=2))

##자꾸 랜덤출력해서 인덱스를 key로 넣음(딕셔너리)