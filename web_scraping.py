import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

TitleData = soup.findAll(class_="titleColumn")

titles = []

for title in TitleData:
    titles.append(title.find('a').get_text())

with open(r'C:\Users\rknav\Downloads\movies.csv', "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(['Title'])
    for title in titles:
        wr.writerow([title])

print('files created successfully')

