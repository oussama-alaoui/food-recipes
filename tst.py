from inspect import isframe
from pickle import APPEND
import requests 
from bs4 import BeautifulSoup
import csv
import re
import time
from itertools import zip_longest



cuisine = ["meat", "fruit", "vegetables", "dairy", "grains-pulses", "banana-recipes", "chocolate", "coffee"]


#get number of page
for a in range(0, len(cuisine)):
    
	myfile = open("./"+cuisine[a]+".csv", "a")
	wr = csv.writer(myfile)
	wr.writerow(["name", "image", "time", "ingredient", "nutrition", "categoty", "methode"])
	print("Cuisine: %s" % cuisine[a])

	#find number of page
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
		print("	page %d/%d" % (i, page))
		result = requests.get("https://www.bbcgoodfoodme.com/collections/"+cuisine[a]+"/?page="+str(i))
		src = result.content
		soup = BeautifulSoup(src, "lxml")
		#find all url of recipe
		box = soup.find('div', {'class': 'list-row'}).find("ul").find_all("li")
		j = 1
		for row in box:
			print("		product %d" % j)
			#find url of recipe
			url = row.findChildren('a')[0]['href']
			
      		#find name of recipe
			recipe_name = row.findChildren('a')[0].text
			
			#find image of recipe
			recipes_image = row.findChildren('img')[0]['data-src']
			
			# find preparation time of recipe
			result = requests.get(url)
			src = result.content
			soup = BeautifulSoup(src, "lxml")
			prep_time = soup.find("span", {"class": "text"})
			prep_time = prep_time.text
			prep_time = prep_time.replace("\n", "")
			prep_time = prep_time.replace("\t", "")
			prep_time = prep_time.replace("\r", "")
			prep_time = prep_time.replace(" ", "")
			prep_time = prep_time.replace("mins", "")
			prep_time = prep_time.replace("min", "")
			recipe_time = prep_time

			
   			# find ingredients of recipe
			ingredient = soup.find("div", {"class": "ingredient-list"})
			ingredient = ingredient.find_all("li")
			recipe_ingredient_recipe = []
			for y in range(0, len(ingredient)):
				ingredient[y] = ingredient[y].text
				ingredient[y] = ingredient[y].replace("\u200b", "")
				ingredient[y] = ingredient[y].replace("\u2044", "/")
				recipe_ingredient_recipe.append(ingredient[y])
			recipe_ingredient_all =recipe_ingredient_recipe

			#find nutrition of recipe
			nutrition = soup.find("ul", {"class": "nutrition-list"})
			nutrition = nutrition.find_all("li")
			recipe_nutrition_recipe = []
			for y in range(0, len(nutrition)):
				nutrition[y] = nutrition[y].text
				nutrition[y] = nutrition[y].replace("\u200b", "")
				nutrition[y] = nutrition[y].replace("\u2044", "/")
				nutrition[y] = nutrition[y].replace("\n", "")
				nutrition[y] = nutrition[y].replace("\t", "")
				recipe_nutrition_recipe.append(nutrition[y])
			recipe_nutrition_all = recipe_nutrition_recipe

			# find method of recipe
			method = soup.find("div", {"class": "method-list"})
			method = method.find_all("li")
			recipe_methode_recipe = []
			for y in range(0, len(method)):
				method[y] = method[y].text
				method[y] = method[y].replace("\u200b", "")
				method[y] = method[y].replace("\u2044", "/")
				method[y] = method[y].replace("\n", "")
				method[y] = method[y].replace("\t", "")
				recipe_methode_recipe.append(method[y])
			recipes_methode_all = recipe_methode_recipe
			wr.writerow([recipe_name, recipes_image, recipe_time, recipe_ingredient_all, recipe_nutrition_all, cuisine[a], recipes_methode_all])
			j += 1
		j = 1
	# # write in csv
	# for l in range(0, len(recipe_name)):
	# # 	
	# 	print(recipes_image[l])