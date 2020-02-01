from bs4 import BeautifulSoup
import requests,pprint,os,json,string
from task1 import data
_url=[]
movies = []
for u in data:
	_url.append(u["url"])
for i in _url:
	file_name=(i[27:36])+".json"
	if os.path.exists("jsonfiles/"+file_name):
		with open("jsonfiles/"+file_name,"r") as file:
			data1 = json.load(file)
			data1 = json.loads(data1)
			movies.append(data1)
	else:
		dict1 = {}
		urll=requests.get(i)
		soup1=BeautifulSoup(urll.text,"html.parser")

		# i am finding name
		soup2=soup1.find("div",class_="title_wrapper").h1.text
		name=""
		for i in soup2:
			if i=="(":
				break
			else:
				name+=i
		name=name.replace("\xa0",'')
		# print(name)

		# here i am finding director
		dir1=soup1.find("div",class_="credit_summary_item")
		d = dir1.findAll("a")
		director=[]
		for dc in d:
			director.append(dc.text)
		# print(director)

		# here i am finding language and countory
		lan=soup1.findAll("div",class_="txt-block")
		language=[]
		for i in lan:
			if 'Language' in i.text:
				lan_a=i.find_all("a")
				for j in lan_a:
					language.append(j.text)
			if "Country" in i.text:
				country=i.find("a").text
		# print(language)
		# print(country)


		# here i am finding poster url
		url_code=soup1.find("div",class_="poster")
		url=url_code.find('img')['src']
		# print(url)

		# here i am finding time
		time=soup1.find("div",class_="subtext")
		run = time.find("time").text.strip()
		print(run)
		digit = "0123456789"
		hour = "0"
		mint = "0"
		runtime=0
		flag = True
		for d in run:
			if (d in digit) and flag:
				hour+=d
			if d=="h":
				flag=False
			if (d in digit and flag==False):
				mint+=d
		runtime+=int(hour)*60+int(mint)
		# print(runtime)

		# here i am finding geners
		genres1=soup1.find_all("div",class_="see-more inline canwrap")
		genres=[]
		for j in genres1:
			if "Genres" in j.text:
				genre=j.findAll("a")
				for y in genre:
					genres.append(y.text)
		# print(genres)


		# here i am finding bio
		bio=soup1.find("div","summary_text").text.strip("\n").strip()
		# print (bio)

		# here i am appending all data in dict1
		dict1["name"]=name
		dict1["runtime"]=runtime
		dict1["language"]=language
		dict1["director"]=director
		dict1["country"]=country
		dict1["bio"]=bio
		dict1["geners"]=genres
		with open("jsonfiles/"+file_name,"w+") as file:
			data1 = json.dumps(dict1)
			json.dump(data1,file)
		movies.append(dict1)
pprint.pprint(movies)
