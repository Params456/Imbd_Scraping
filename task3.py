from task1 import data
from pprint import pprint
decade = {}
for movie in data:
	year = str(movie["year"])
	year=year[:-1]+"0"
	year = int(year)
	if year not in decade:
		decade[year]=[]
		decade[year].append(movie)
	else:
		decade[year].append(movie)
pprint(decade)