# pomocny subor pre pracu s databazou

import pymongo
from bson.objectid import ObjectId

conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products
cdb=mydb.categories
bdb=mydb.brands
# db.insert_many(productsList)
# db.delete_many({})

# products=db.find({"Eshop": "notino"})

# for p in products:
#     db.update_one({"_id": ObjectId(p["_id"])}, 
#                   { "$set":
#                   {"Name": p["Name"],
#                     "Brand": p["Brand"], 
#                     "Price": p["Price"], 
#                     "Category": p["Category"], 
#                     "Url": p["Url"], 
#                     "Image": p["Image"],
#                     "Eshop": "notino"}},
#                   upsert=True)

# cdb.delete_many({})
# bdb.delete_many({})