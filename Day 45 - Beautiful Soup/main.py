import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
webpage = response.text
movie_list = []

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")

for title in titles:
    movie_list.append(title.getText())

movie_list.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in movie_list:
        file.write(f"{title}\n")





