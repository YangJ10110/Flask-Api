from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort
import json
import uuid
from db import stores, items
from schema import ItemSchema, ItemUpdateSchema


blp = Blueprint("store_item", __name__, description="Store operations")

@blp.route("/items")
class Items(MethodView):
    def get(self):
        if not stores:
            abort(404, message="No store items yet")
        else:
            return stores
    
    @blp.arguments(ItemSchema)
    def post(self, store_data):
        #store_data = request.get_json()
        return store_data

    def delete(self):
        return "no"

@blp.route("/items/<store_id>/")
class Store_Items(MethodView):
    def get(self, store_id):
        try:
            return f"ID: {store_id}"
        except TypeError:
            abort(404, message = "Store not found")
        
    def delete(self, store_id):
        return store_id