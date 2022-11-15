from itertools import count
from math import prod
import re
from flask import Flask, jsonify, render_template, request, send_file
from flask_cors import CORS
from mongo import Mongo
from flask_paginate import Pagination, get_page_parameter, get_page_args

app = Flask(__name__)
db = Mongo()
db.connect()

CORS(app, support_credentials=True)


@app.route('/')
def index():
   data = {
      'categories': db.get_categories(),
      'brands': db.get_brands()
   }
   return render_template('index.html', data=data)


@app.route('/databases')
def get_databases():
   return jsonify(db.list_databases())

@app.route('/products')
def get_products():
   q = {}
   if 'brand' in request.args and request.args['brand']:
      q.update({"Brand": request.args['brand']})
   if 'category' in request.args and request.args['category']:
      q.update({"Category": request.args['category']}) 
   if 'name' in request.args and request.args['name']:
      regex = re.compile('.*' + request.args['name'] + ".*", re.IGNORECASE)
      q.update({"Name": regex})
   page=request.args.get(get_page_parameter(), type=int, default=1)  
   per_page = request.args.get("per_page", 21, type=int) 
   products = db.get_products(query=q, currentPage=page)
   allproducts = db.get_all_products(query=q)
   total=len(allproducts)
   pagination=Pagination(page=page, per_page=per_page, total=total, record_name='products')
   return render_template('products.html', products=products, pagination=pagination, page=page,per_page=per_page)

@app.route('/categories')
def get_categories():
   return jsonify(db.get_distinct_categories())

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)