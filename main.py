import requests, re
from bs4 import BeautifulSoup

response = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=hp+255&_sacat=0")

soup = BeautifulSoup(response.text, "html.parser")

product_name = soup.find_all("li", class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")

for name in product_name:
    product_name = name.find("div", class_="s-item__title").span.text
    actual_price = name.find("span", class_="s-item__price").text if name.find("span", class_="s-item__price").text[0] == "$" else "n/a"
    discount = name.find_all("div", class_="s-item__detail s-item__detail--primary")[1].text
    # discount_price = discount[discount.index("Previous Price")+1:] if discount.find("Was") else "n/a"
    print(product_name, actual_price, discount)
