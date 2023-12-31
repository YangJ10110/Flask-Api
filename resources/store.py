from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort
import json
import uuid
from db import stores, items

from schema import ItemSchema, ItemUpdateSchema, StoreSchema


blp = Blueprint("stores", __name__, description="Store operations")

@blp.route("/stores")
class Stores(MethodView):
    
    def get(self):
        if not stores:
            abort(404, message="No stores yet")
        else:
            return "stores"
    
    def put(self):
        return ""
    
    @blp.arguments(StoreSchema)
    def post (self, store_data):
        return store_data
        
    def delete(self):
        return ""

@blp.route("/stores/<store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return f"ID: {store_id}"
        except TypeError:
            abort(404, message = "Store not found")
        
    def delete(self, store_id):
        return store_id