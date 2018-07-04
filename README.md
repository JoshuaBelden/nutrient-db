Nutrient Analysis
===========

Nutrient-db (https://github.com/schirinos/nutrient-db) is a program to convert the USDA National Nutrient Database for Standard Reference (http://www.ars.usda.gov/ba/bhnrc/ndl) from the flat files they provide into a relational database. Let's see what interesting observations we can learn from it. Note that these require **Python3.x**.

Using k-means analysis (explained in the presentation), you can see if it makes sense to separate foods into 2, 3, 4... groups. Can the computer "learn" what the food groups are from nutrition data?

**nutrientslist.py** - Simply lists each nutritional value.

**kmeansclick.py** - Click various points, and close each window to see the next k-mean clustering. Which separation fits best?

**foodcluster.py** Tries to cluster the USDA database intro food groups. Spoiler alert, they are very separable into 2,3,4, or 5 groups. After running this, note the central foods of each group and read outputs in (NClusters-n) output files.

```
For 5 clusters the average silhouette score is 0.840297
#1 Turnover, filled with egg, meat and cheese, frozen off by 607.120245
#2 HOT POCKETS, CROISSANT POCKETS Chicken, Broccoli, and Cheddar Stuffed Sandwich, frozen off by 607.120245
#3 HOT POCKETS, CROISSANT POCKETS Chicken, Broccoli, and Cheddar Stuffed Sandwich, frozen off by 607.120245


#1 Veal, variety meats and by-products, liver, cooked, braised off by 37625.011750
#2 Beef, New Zealand, imported, variety meats and by-products liver, cooked, boiled off by 37625.011750
#3 Beef, New Zealand, imported, variety meats and by-products liver, cooked, boiled off by 37625.011750


#1 Beef, variety meats and by-products, liver, cooked, braised off by 17710.545346
#2 Beef, variety meats and by-products, liver, cooked, pan-fried off by 17710.545346
#3 Beef, variety meats and by-products, liver, cooked, pan-fried off by 17710.545346


#1 Peas and carrots, frozen, cooked, boiled, drained, with salt off by 6637.241690
#2 Peas and carrots, frozen, cooked, boiled, drained, without salt off by 6637.241690
#3 Peas and carrots, frozen, cooked, boiled, drained, without salt off by 6637.241690


#1 Tomato products, canned, sauce, with onions, green peppers, and celery off by 2211.156050
#2 Tomato products, canned, sauce, with mushrooms off by 2211.156050
#3 Tomato products, canned, sauce, with mushrooms off by 2211.156050
```


USDA National Nutrient Database for Standard Reference (http://www.ars.usda.gov/ba/bhnrc/ndl)

