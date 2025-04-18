#MapPlot.py
#Name:
#Date:
#Assignment:

import matplotlib.pyplot as plt
import nuclear_explosions

nukes = nuclear_explosions.get_nuclear_explosion()

usaYearlyDetonations = {}

for nuke in nukes:
    country = nuke["Location"]["Country"]
    year = nuke["Date"]["Year"]

    if country == "USA":
        if year in usaYearlyDetonations:
            usaYearlyDetonations[year] += 1
        else:
            usaYearlyDetonations[year] = 1

years = []
num = []

for year in usaYearlyDetonations:
    years.append(year)
    num.append(usaYearlyDetonations[year])

plt.figure(figsize=(10, 5))
plt.plot(years, num, 'ro')
plt.title("Number of US Nuclear Detonations per Year")
plt.xlabel("Year")
plt.ylabel("Number of Detonations")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.savefig("output")