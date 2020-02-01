from task1 import data
from pprint import pprint
dict1={}
for movie in data:
	if movie["year"] not in dict1:
		dict1[movie["year"]]=[]
		dict1[movie["year"]].append(movie)
	else:
		dict1[movie["year"]].append(movie)
pprint(dict1)
