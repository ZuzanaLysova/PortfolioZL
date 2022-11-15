# -*- coding: utf-8 -*-
from weakref import ref
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products
bdb=mydb.brands


allBrands = db.find({}, {"Brand":True, "_id":False}).distinct("Brand")
searchedBrands = db.find({"Eshop": "makeup"}, {"Brand":True, "_id":False}).distinct("Brand")
def get_distinct_brands():
    brands={}
    for b in allBrands:
        for x in searchedBrands:
            ratioNum=fuzz.ratio(b, x)
            if ratioNum > 85:
                if not b in brands:
                    brands[b] = x
    return brands

ref_brands = get_distinct_brands()
for b in allBrands:
  if b not in ref_brands.keys():
    ref_brands[b] = b

products=db.find()

for p in products:
    if p['Brand'] in ref_brands:
        db.update_one({"_id": ObjectId(p["_id"])}, { "$set": {"Brand": ref_brands[p["Brand"]]}})

brandsList=[]     

brandsList=list(db.distinct("Brand"))
for b in brandsList:
    bdb.insert_one({"Brand": b})
