import requests
from bs4 import BeautifulSoup

data = requests.get("http://web.archive.org/web/20200502230122/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = data.text

soup = BeautifulSoup(website_html, "html.parser")
movies_data = soup.find_all(name="h3", class_="title")

movie_rankings = [(item.getText()) for item in movies_data]
movies = (movie_rankings[::-1])

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")