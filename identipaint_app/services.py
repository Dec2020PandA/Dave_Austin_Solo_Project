import requests
from identipaint.keys import ACCESS_KEY, SECRET_KEY

API_URL = "https://www.wikiart.org/en/"


def new_session():
    return requests.get(
        API_URL + "Api/2/login?accessCode=" + ACCESS_KEY + "&secretCode=" + SECRET_KEY
    ).json()["SessionKey"]


def get_artists():
    return requests.get(
        API_URL
        + "api/2/ArtistsByDictionary?&group=1&dictUrl=minimalism&"
        + "authSessionKey="
        + request.session["session_key"]
    ).json()


def get_paintings(artist):
    return requests.get(
        API_URL
        + "App/Painting/PaintingsByArtist?artistUrl="
        + artist
        + "&json=2&authSessionKey="
        + request.session["session_key"]
    ).json()
