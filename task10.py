from task5 import movies
from pprint import pprint
dire_lang = {}
for movie in movies:
	for dire in movie["director"]:
		if dire not in dire_lang:
			dire_lang[dire]={}
			for lang in movie["language"]:
				if lang not in dire_lang[dire]:
					dire_lang[dire][lang]=1
				else:
					dire_lang[dire][lang]+=1
	else:
		for lang in movie["language"]:
			if lang not in dire_lang[dire]:
				dire_lang[dire][lang]=1
			else:
				dire_lang[dire][lang]+=1
# pprint(dire_lang)