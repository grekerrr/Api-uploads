from pprint import pprint
import requests


TOKEN = "2619421814940190"


heroes_list = ["Hulk", "Captain America", "Thanos"]


def heroes_intelligence(list):
    heroes_intelligence = {}
    for hero_name in list:
        url = f"https://superheroapi.com/api/{TOKEN}/search/{hero_name}"
        response = requests.get(url)
        heroes_intelligence[hero_name] = int(response.json()["results"][0]["powerstats"]["intelligence"])
    return heroes_intelligence


def comparison(dict):
    max_intelligence = max(dict.values())
    value_s = list(dict.values())
    key_s = list(dict.keys())
    best_hero_name = key_s[value_s.index(max_intelligence)]
    print(f"Самый умный: {best_hero_name}, его интеллект: {max_intelligence}")


# pprint(heroes_intelligence(heroes_list))
comparison(heroes_intelligence(heroes_list))

