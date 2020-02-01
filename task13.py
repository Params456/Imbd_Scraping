from task5 import movies
from bs4 import BeautifulSoup
import requests,pprint,os,json
if os.path.exists("jsonfiles/name_of_movies.json"):
	list2=[]
	with open ("jsonfiles/name_of_movies.json","r") as files:
		names=json.loads(json.load(files))
		# pprint.pprint(names)
	for ii in range(len(names)):
		aa=names[ii]
		with open("jsonfiles/"+aa+".json",'r') as thamu:
			thaman=json.load(thamu)
			thaman=json.loads(thaman)
		# pprint.pprint(thaman)
		a=requests.get("https://www.imdb.com/title/"+aa+"/fullcredits?ref_=tt_cl_sm#cast")
		b=BeautifulSoup(a.text,"html.parser")
		c=b.find("table",class_="cast_list")
		d=c.findAll("td",class_="")
		list1=[]
		for j in d:
			di={}
			e=j.find("a")
			h=e.text
			name=h.strip("\n")
			f=j.find("a")["href"]
			imdb_id=f[6:15]
			di["name"]=name
			di["imdb_id"]=imdb_id
			list1.append(di.copy())
		thaman["cast"]=list1
		list2.append(thaman	)
	pprint.pprint(list2)
	with open("poga.json","w+") as ruby:
		paran=json.dumps(list2)
		thaman=json.dump(paran,ruby)	