import numpy as np
from pandas import read_csv

data = read_csv("slaughter-list.csv")

addresses = [i.strip() for i in np.char.add(np.array(data["Street Address"].tolist(), dtype=str), np.array([" "+x for x in data["City"].tolist()], dtype=str)).tolist()]

print(addresses)
