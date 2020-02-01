from task5 import movies
lang = {}
for movie in movies:
	for language in movie["language"]:
		if language not in lang:
			lang[language]=1
		else:
			lang[language]+=1
print(lang)