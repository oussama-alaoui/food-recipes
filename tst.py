from inspect import isframe
from pickle import APPEND
import requests 
from bs4 import BeautifulSoup
import csv
import re
import time
from itertools import zip_longest



myfile = open("C:\\Users\\Alaoui\\Desktop\\food recipes\\movies2.csv", "a")
wr = csv.writer(myfile)
# wr.writerow(["movi_name", "movi_image", "movi_hestory", "movi_url_video", "type"])
cuisine = ["chinese", "italian"]
recipe_url = []
recipe_name = []
recipes_image = []
recipe_ingredient = []


#get number of page
for a in range(0, 1):
	#chack all page whit number
	result = requests.get("https://www.bbcgoodfoodme.com/collections/"+cuisine[a]+"/")
	src = result.content
	soup = BeautifulSoup(src, "lxml")
 
 
	#find number of page
	page = soup.find("div", {"class": "pagination"})
	page = page.find_all("a")
	page = page[-2].text
	page = int(page)
 
	#get all url of page
	for i in range(1, page+1):
		result = requests.get("https://www.bbcgoodfoodme.com/collections/"+cuisine[a]+"/?page="+str(i))
		src = result.content
		soup = BeautifulSoup(src, "lxml")
		#find all url of recipe
		recipe = soup.find_all("a", {"rel": "bookmark"})
		for i in range(0, len(recipe)):
			
			#find url of recipe
			url = recipe[i]["href"]
   		# 	#find name of recipe
		# 	recipe_name.append(recipe[i].text)
			
   		# 	#find image of recipe
		# 	# image = soup.find("img", {"class": "img-responsive"})
		# 	# recipes_image.append(image["data-src"])

			#find preparation time of recipe
			# result = requests.get(url)
			# src = result.content
			# soup = BeautifulSoup(src, "lxml")
			# prep_time = soup.find("span", {"class": "text"})
			# prep_time = prep_time.text
			# prep_time = prep_time.replace("\n", "")
			# prep_time = prep_time.replace("\t", "")
			# prep_time = prep_time.replace("\r", "")
			# prep_time = prep_time.replace(" ", "")
			# prep_time = prep_time.replace("mins", "")
			# prep_time = prep_time.replace("min", "")
			# #find ingredients of recipe
			# ingredient = soup.find("div", {"class": "ingredient-list"})
			# ingredient = ingredient.find_all("li")
			# for y in range(0, len(ingredient)):
			# 	ingredient[y] = ingredient[y].text
			# 	ingredient[y] = ingredient[y].replace("\u200b", "")
			# 	ingredient[y] = ingredient[y].replace("\u2044", "/")
			# 	recipe_ingredient.append(ingredient[y].text+"/")

			#find method of preparation of recipe
			method = soup.find("div", {"class": "method-list"})
			method = method.find_all("li")
			for y in range(0, len(method)):
				# recipe_ingredient.append(method[y].text+"/")
				print(method[y].text)


			# #write in csv
			# wr.writerow([name, image, story, video, type])