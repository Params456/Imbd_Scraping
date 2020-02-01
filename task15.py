import json,os
from pprint import pprint

director={}
if os.path.exists("poga.json"):
	with open("poga.json","r") as ruby:
		paran=json.load(ruby)
		list2=json.loads(paran)
	for list1 in list2:	
		for cast in list1["cast"]:
			ca=cast["imdb_id"]
			if ca not in director:
				director[ca]={}
				director[ca]["name"]=cast["name"]
				director[ca]['num_of_movie']=1
			else:
				director[ca]['num_of_movie']+=1
pprint(director)