import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="a-no-trucate")

titles = [title.getText().strip() for title in titles]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Fawaz",
    )
)
user_id = sp.current_user()["id"]

uri_list = []
year = date.split("-")[0]

for song in titles:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)