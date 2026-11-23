import re
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
vocabulary = ['.'] + vocabulary

char_to_id = {char: i for i, char in enumerate(vocabulary)}
id_to_char = dict(enumerate(vocabulary))

#Write an encode(name) function that returns a tensor of IDs, and a decode(tensor) function that turns it back into a string.
def encode(name: str) -> torch.Tensor:
    ids = []
    for c in name:
        ids.append(char_to_id[c])
        
    return torch.tensor(ids)
    


def decode(tensor: torch.Tensor) -> str:
    name = ""
    ids = tensor.tolist()
    for i in ids:
        name += id_to_char[i]
        
    return name

if __name__ == "__main__":
    print("vocabulary size:", len(vocabulary))
    encodechu = encode(".pikachu")
    print(encodechu)
    print(encodechu.dtype)
    print(decode(encodechu))
