from bs4 import BeautifulSoup
import requests,pprint,os,json
a=requests.get("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")
b=BeautifulSoup(a.text,"html.parser")
c=b.find("table",class_="cast_list")
d=c.findAll("td",class_="")
list1=[]
for i in d:
	di={}
	e=i.find("a")
	h=e.text
	name=h.strip("\n")
	f=i.find("a")["href"]
	imdb_id=f[6:15]
	di["name"]=name
	di["imdb_id"]=imdb_id
	list1.append(di.copy())
pprint.pprint(list1)