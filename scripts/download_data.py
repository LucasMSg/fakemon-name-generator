from pathlib import Path
from urllib.request import urlopen, Request
import json

url = "https://pokeapi.co/api/v2/pokemon-species?limit=2000"
req = Request(url, headers={"User-Agent": "my-fakemon-script/1.0"})

with urlopen(req) as response:
    data = json.load(response)

path = Path("./data/pokemon.txt")
path.parent.mkdir(parents=True, exist_ok=True)

written = 0
with open(path, "w") as f:
    for species in data["results"]:
        f.write(species["name"] + "\n")
        written += 1

assert written == data["count"], f"wrote {written}, expected {data['count']}"