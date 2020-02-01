import json
from pprint import  pprint
with open ("poga.json") as thaman:
	a=json.load(thaman)
	b=json.loads(a)

list1=[]
for i in b:
	imdb_id=i["cast"]
	list1.append(imdb_id)
# pprint(list1)
dict1={}
for j in list1:
	for k in range(1,len(j)):
		# pprint(k)
		if j[0]["imdb_id"] not in dict1:
			dict1[j[0]["imdb_id"]]={}
			dict1[j[0]["imdb_id"]]["name"]=j[0]["name"]
			dict1[j[0]["imdb_id"]]["frequent_co_actors"]=[]
			dict2={}
			if j[k]["imdb_id"] not in dict2:		
				dict2["name"]=j[k]["name"]
				dict2["imdb_id"]=j[k]["imdb_id"]
				dict2["num_movies"]=1
			else:
				dict2["num_movies"]+=1
			dict1[j[0]["imdb_id"]]["frequent_co_actors"].append(dict2)
		else:
			for ii in dict1:
				if ii==j[0]["imdb_id"]:
					dict2={}
					if j[k]["imdb_id"] not in dict2:
						dict2["name"]=j[k]["name"]
						dict2["imdb_id"]=j[k]["imdb_id"]
						dict2["num_movies"]=1
					else:
						dict2["num_movies"]+=1

					dict1[j[0]["imdb_id"]]["frequent_co_actors"].append(dict2)
pprint(dict1)
a=input("Enter the name: ")
for ji in dict1:
	if ji==a:
		pprint(dict1[ji])
