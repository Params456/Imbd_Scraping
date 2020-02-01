from task5 import movies
dire = {}
for movie in movies:
	for director in movie["director"]:
		if director not in dire:
			dire[director]=1
		else:
			dire[director]+=1
print(dire)