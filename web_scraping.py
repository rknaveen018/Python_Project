from bs4 import BeautifulSoup
import requests, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Top 250 Movies"
sheet.append(["Rank", "Movie Name", "Rating", "Year of release"])

try:
    response = requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(response.text, "html.parser")
    movie = soup.find("tbody", class_="lister-list").find_all("tr")

    for movies in movie:
        rank = movies.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
        movie_name = movies.find("td", class_ ="titleColumn").a.text
        rating = movies.find("td", class_="ratingColumn imdbRating").strong.text
        year = movies.find("td", class_="titleColumn").span.text.replace("("," ")
        year = year.replace(")"," ")
        sheet.append([rank, movie_name, rating, year])
except Exception as e:
    print(e)

wb.save(r"C:\Users\rknav\Downloads\Movie_list.xlsx")