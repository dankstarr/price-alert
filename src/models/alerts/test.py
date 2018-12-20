from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/gp/product/B01MR4VOBZ/ref=ox_sc_act_title_2?smid=ATVPDKIKX0DER&psc=1"
h = {'User-Agent': 'Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}

request = requests.get(url, verify=False, headers=h)
content = request.content
print("content is" + str(content))
str = str(content)
spl = str.split("<body", 1)[1]
print("split is" + spl)
body = "<body"
body = "".join((body, spl))
print("body is" + body)
endbody = str.split("/body>", 1)[1]
new = body.replace(endbody, "")
print("new is " + new)

soup = BeautifulSoup(content, "lxml")

fin = soup.find('span',  {'id': 'priceblock_ourprice', 'class': 'a-size-medium a-color-price'}).text

print(fin)
