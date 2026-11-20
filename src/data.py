import re
import string
import torch
from pathlib import Path

path = Path("./data/pokemon.txt")
treated_data = []

with open(path, encoding="utf-8") as f:
#cleaning numbers
    for line in f:
        name = line.strip()
        if name and not re.search(r"[0-9]", name):
           treated_data.append(name)
                       
vocabulary = []

for names in treated_data:
    for c in names:
        if c not in vocabulary:
            vocabulary.append(c)

vocabulary.sort()
print(vocabulary)

chart_to_id = {char: i for i, char in enumerate(vocabulary)}
id_to_char = dict(enumerate(vocabulary))
print(chart_to_id)
print(id_to_char)

#Write an encode(name) function that returns a tensor of IDs, and a decode(tensor) function that turns it back into a string.
def encode(name: string) -> torch.tensor:
    ids = []
    for c in name:
        ids.append(chart_to_id[c])
        
    return torch.tensor(ids)
    
print(encode("pikachu"))

def decode(tensor: torch.tensor) -> string:
    name = ""
    ids = tensor.tolist()
    for i in ids:
        name += id_to_char[i]
        
    return name

print(decode(encode("pikachu")))
