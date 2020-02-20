# %%
# %%
import numpy as np
import pandas as pd

# %%
content = None

with open('data/a_example.txt') as f:
    line1 = f.readline()
    line2 = f.readline()
    content = f.readlines()


print(content)


print(line1)

print(line2)
# %%
# fist lines
parts = [int(s) for s in line1.split(' ')]

bookNumber = parts[0]
libraryNumber = parts[1]
daysForScanning = parts[2]

bookScores = [int(s) for s in line2.split(' ')]

# %%

for i in range(0, libraryNumber * 2, 2):
    parts = [int(s) for s in content[i].split(' ')]

    libBooksNumber = parts[0]
    libSignUpTime = parts[1]
    libBookPerDay = parts[2]

    libBookIds = [int(s) for s in content[i + 1].split(' ')]

    print(libBookIds)







