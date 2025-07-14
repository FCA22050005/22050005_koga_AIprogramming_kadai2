import requests
import csv
from pathlib import Path

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    json_data = response.json()
    return {
        "name": json_data["name"],
        "image_url": json_data["sprites"]["front_default"],
        "types": [t["type"]["name"] for t in json_data["types"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in json_data["stats"]}
    }

def save_search_history(name):
    history_path = Path("data/search_history.csv")
    history_path.parent.mkdir(parents=True, exist_ok=True)
    with open(history_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name])
