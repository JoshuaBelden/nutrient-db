#!/usr/bin/python3
"""Parses USDA, simply lists nutrients."""
import nutrientdb
db = nutrientdb.NutrientDB() #empty () since not setting db, default.
for food in db.database.execute('select NDB_no, Long_Desc, ManufacName from food_des'):
	g = db.query_gramweight(food['NDB_no'])
	print('100g of %s has:' % (food['Long_Desc'],))
	for nutrient in db.query_nutrients(food['NDB_no']):
		del nutrient['meta']
		print(nutrient)
	print('\n\n\n\n\n')
