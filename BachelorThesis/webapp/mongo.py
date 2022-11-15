from unicodedata import category
from pymongo import MongoClient
from bson.code import Code
from bson.objectid import ObjectId
from datetime import datetime
import dns.resolver
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']


class Mongo():
    
    ########### PRIPOJENIE ###########
    
    def __init__(self):
        super().__init__()
        self.client = None
        self.collection = None
    
    def connect(self):
        self.client = MongoClient("mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/Products?retryWrites=true&w=majority")
   
    def disconnect(self):
        self.client.close()

    def list_databases(self):
        return self.client.list_database_names()
    
    ########### PRODUKTY ###########
    
    # Vrati list vsetkych produktov (po 21)
    # Mozno doplnit query
    def get_products(self, query={}, currentPage=1):
        return list(self.client.Products.products.find(query).skip((currentPage-1)*21).sort("Price").limit(21))

    # Vrati list uplne vsetkych produktov
    def get_all_products(self, query={}):
        return list(self.client.Products.products.find(query))

    ########### KATEGORIE ###########
    def get_categories(self):
        return list(self.client.Products.categories.distinct('Category'))

    ########### ZNACKY ###########
    def get_brands(self):
        return list(self.client.Products.brands.distinct('Brand'))
