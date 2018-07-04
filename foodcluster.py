#!/usr/bin/python3
import numpy
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt

class FoodDef:
	def __init__(self, name):
		self.name = name
		self.data = {}
		
	def add(self, name, amount):
		"""
		associate a nutrient - by name (g of proten for example)
		per 100g.
		"""
		self.data[name] = amount
	
	def getArr(self):
		"""
		Return a raw array appropriate for machine learning functions.
		"""
		return [self.data[name] if name in self.data else 0 for name in ['Protein',
'Total lipid (fat)',
'Carbohydrate, by difference',
'Ash',
'Energy',
#'Alcohol, ethyl',
'Water',
'Caffeine',
'Theobromine',
'Energy',
'Sugars, total',
'Fiber, total dietary',
'Calcium, Ca',
'Iron, Fe',
'Magnesium, Mg',
'Phosphorus, P',
'Potassium, K',
'Sodium, Na',
'Zinc, Zn',
'Copper, Cu',
'Manganese, Mn',
'Selenium, Se',
'Vitamin A, IU',
'Retinol',
'Vitamin A, RAE',
'Carotene, beta',
'Carotene, alpha',
'Vitamin E (alpha-tocopherol)',
'Vitamin D',
'Vitamin D3 (cholecalciferol)',
'Vitamin D (D2 + D3)',
'Cryptoxanthin, beta',
'Lycopene',
'Lutein + zeaxanthin',
'Vitamin C, total ascorbic acid',
'Thiamin',
'Riboflavin',
'Niacin',
'Pantothenic acid',
'Vitamin B-6',
'Folate, total',
'Vitamin B-12',
'Choline, total',
#'Dihydrophylloquinone',
'Vitamin K (phylloquinone)',
'Folic acid',
'Folate, food',
'Folate, DFE',
#'Betaine',
'Tryptophan',
'Threonine',
'Isoleucine',
'Leucine',
'Lysine',
'Methionine',
'Cystine',
'Phenylalanine',
'Tyrosine',
'Valine',
'Arginine',
'Histidine',
'Alanine',
'Aspartic acid',
'Glutamic acid',
'Glycine',
'Proline',
'Serine',
#'Hydroxyproline',
'Vitamin E, added',
'Vitamin B-12, added',
'Cholesterol',
'Fatty acids, total saturated']]

nutrientNames = ['Protein',
'Total lipid (fat)',
'Carbohydrate, by difference',
'Ash',
'Energy',
#'Alcohol, ethyl',
'Water',
'Caffeine',
'Theobromine',
'Energy',
'Sugars, total',
'Fiber, total dietary',
'Calcium, Ca',
'Iron, Fe',
'Magnesium, Mg',
'Phosphorus, P',
'Potassium, K',
'Sodium, Na',
'Zinc, Zn',
'Copper, Cu',
'Manganese, Mn',
'Selenium, Se',
'Vitamin A, IU',
'Retinol',
'Vitamin A, RAE',
'Carotene, beta',
'Carotene, alpha',
'Vitamin E (alpha-tocopherol)',
'Vitamin D',
'Vitamin D3 (cholecalciferol)',
'Vitamin D (D2 + D3)',
'Cryptoxanthin, beta',
'Lycopene',
'Lutein + zeaxanthin',
'Vitamin C, total ascorbic acid',
'Thiamin',
'Riboflavin',
'Niacin',
'Pantothenic acid',
'Vitamin B-6',
'Folate, total',
'Vitamin B-12',
'Choline, total',
#'Dihydrophylloquinone',
'Vitamin K (phylloquinone)',
'Folic acid',
'Folate, food',
'Folate, DFE',
#'Betaine',
'Tryptophan',
'Threonine',
'Isoleucine',
'Leucine',
'Lysine',
'Methionine',
'Cystine',
'Phenylalanine',
'Tyrosine',
'Valine',
'Arginine',
'Histidine',
'Alanine',
'Aspartic acid',
'Glutamic acid',
'Glycine',
'Proline',
'Serine',
#'Hydroxyproline',
'Vitamin E, added',
'Vitamin B-12, added',
'Cholesterol',
'Fatty acids, total saturated']

import nutrientdb
db = nutrientdb.NutrientDB() #empty () since not setting db, default.
foods = [];
i = 0
for food in db.database.execute('select NDB_no, Long_Desc, ManufacName from food_des'):
	#g = db.query_gramweight(food['NDB_no'])
	#print('100g of %s has:' % (food['Long_Desc'],))
	thisFood = FoodDef(food['Long_Desc'])
	for nutrient in db.query_nutrients(food['NDB_no']):
		del nutrient['meta']
		#print(nutrient)
		thisFood.add( nutrient['name'], nutrient['value'] )
	foods.append(thisFood)
	#limit:
	#i+=1
	#if i>10:
	#	break;

print('Data loaded from db.')
X = [food.getArr() for food in foods]

for C in range(2,11):
	model = KMeans(n_clusters=C, random_state=0)
	model.fit(X)
	print('For %d clusters the average silhouette score is %f' % (C, silhouette_score(X, model.labels_)))
	for i in range(C):
		#output:
		centroids = model.cluster_centers_
		nutrients = centroids[i]
		#print(nutrientNames)
		#for n in range(len(nutrientNames)):
		#	print('%s : %f' % ( nutrientNames[n], nutrients[n] ))
		
		#Find one close food:
		#diff = 100000000
		#closefood = ''
		#for fooditem in foods:
		#	mydiff = numpy.sum( numpy.abs( fooditem.getArr() - nutrients ) )
		#	if mydiff < diff:
		#		diff = mydiff
		#		closefood = fooditem.name
		#print( 'For example, %s off by %f' % (closefood, diff) )
		#More pythonic, and list of all by name:
		diffFoods = [(fooditem, numpy.sum(
		numpy.abs( fooditem.getArr() - nutrients ) ) ) for fooditem in foods]
		items = sorted(diffFoods, key=lambda tupl: tupl[1])
		print('#1 %s off by %f' % ( items[0][0].name, items[0][1]))
		print('#2 %s off by %f' % ( items[1][0].name, items[0][1]))
		print('#3 %s off by %f' % ( items[1][0].name, items[0][1]))
		print('\n')
		
		
		#output different groups:
		with open('%dClusters-%d' % (C, i), 'w') as outfile:
			#output all in i classification:
			for fn in range(len(foods)):
				if model.labels_[fn] == i:
					outfile.write(foods[fn].name+'\n')
