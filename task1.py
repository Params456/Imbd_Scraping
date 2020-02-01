from bs4 import BeautifulSoup
import requests,pprint,os,json


if os.path.exists("jsonfiles/first.json"):
	with open("jsonfiles/first.json","r") as file:
		data = json.load(file)
		data = json.loads(data)
else:
	url=(" https://www.imdb.com/india/top-rated-indian-movies/")
	a=requests.get(url)
	# print(a)
	soup=BeautifulSoup(a.text,"html.parser")
	# print(type(soup))
	soup=soup.find("tbody")
	# print(soup)
	soup=soup.findAll("tr")
	# print(soup)	
	z=0
	_name=[]
	_year=[]
	_ratting=[]
	_url=[]
	_possition=[]

	for i in soup:
		z+=1
		d=i.find("td",class_="titleColumn")
		name=d.find("a")
		year=d.find("span")
		ratting=i.find("strong")
		# print(z)
		# print("name ",name.text)
		# print("year ",year.text.strip("(").strip(")"))
		# print("ratting",ratting.text)
		# print("url",name["href"])
		_name.append(name.text)
		_year.append(year.text.strip("(").strip(")"))
		_ratting.append(ratting.text)
		_url.append("https://www.imdb.com"+name["href"])
		_possition.append(z)
	# print(_possition)
	# print(_name)
	# print(_year)
	# print(_url)
	# print(_ratting)t
	_full=[]
	m=[]
	a=["possition","name","year","url","ratting"]
	for i in range(len(_possition)):
		_full.append([_possition[i],_name[i],_year[i],_url[i],_ratting[i]])
		for j in _full:
			p={}
			for k in range(len(a)):
				p[a[k]]=j[k]
		m.append(p)
	with open("jsonfiles/first.json","w+") as file:
		data = json.dumps(m)
		json.dump(data,file)
# print(data)
