from task5 import movies
generes={}
for movie in movies:
	for genre in movie["geners"]:
		if genre not in generes:
			generes[genre]=1
		else:
			generes[genre]+=1
print(generes)