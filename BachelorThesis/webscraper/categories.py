# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products
cdb=mydb.categories


allCategories = db.find({}, {"Category":True, "_id":False}).distinct("Category")
searchedCategories = db.find({"Eshop": "notino"}, {"Category":True, "_id":False}).distinct("Category")
def get_distinct_categories():
    categories={}
    for c in allCategories:
        for x in searchedCategories:
            ratioNum=fuzz.ratio(c, x)
            if ratioNum > 77:
                if not c in categories:
                    categories[c] = x
    return categories

ref_cats = get_distinct_categories()
for c in allCategories:
  if c not in ref_cats.keys():
    ref_cats[c] = c

products=db.find()

for p in products:
    if p['Category'] in ref_cats:
        db.update_one({"_id": ObjectId(p["_id"])}, { "$set": {"Category": ref_cats[p["Category"]]}})

categoriesList=[]     

categoriesList=list(db.distinct("Category"))
for c in categoriesList:
    cdb.insert_one({"Category": c})
