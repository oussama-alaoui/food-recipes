from inspect import isframe
from pickle import APPEND
import requests 
from bs4 import BeautifulSoup
import csv
import re
import time
from itertools import zip_longest



myfile = open("/Users/oalaoui-/Desktop/food-recipes/movies2.csv", "a")
wr = csv.writer(myfile)
wr.writerow(["name", "image", "time", "ingredient", "nutrition", "categoty", "methode"])
cuisine = ["chinese", "italian"]
recipe_url = []
recipe_name = []
recipes_image = []
recipe_ingredient_all = []
recipe_nutrition_all = []


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
      		#find name of recipe
			recipe_name.append(recipe[i].text)
			# find preparation time of recipe
			result = requests.get(url)
			src = result.content
			soup = BeautifulSoup(src, "lxml")
            
            # find method of recipe


            
            
			# write in csv
			# wr.writerow([recipe_name[i], recipes_image[i], prep_time, recipe_ingredient_all[i], recipe_nutrition_all[i]])