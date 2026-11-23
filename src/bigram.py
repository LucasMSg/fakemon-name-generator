import torch
from data import treated_data, vocabulary, char_to_id


assert char_to_id['.'] == 0, f"{char_to_id['.']} != {0}"

V = len(vocabulary)
counts = torch.zeros((V, V), dtype=torch.int32)

data_with_period = ["." + name + "." for name in treated_data]

for name in data_with_period:
    for c1, c2 in zip(name, name[1:]):
        counts[char_to_id[c1], char_to_id[c2]] += 1
        
expected = sum(len(name) - 1 for name in data_with_period)
assert counts.sum().item() == expected, f"{counts.sum().item()} != {expected}"
print("total pairs:", expected)

#Row 0 is "what comes after .", meaning first letters. Selecting one row of a 2D tensor needs just one index.
#Column 0 is "what comes before .", meaning last letters. Selecting a column means taking every row at column 0. Look up how : works in tensor indexing.
#.argmax() gives you the position of the largest value. That position is an ID, and you already have a way to turn an ID back into a character.

print(counts[0])     # row 0
print(counts[:, 0])  # column 0
print(counts.argmax())