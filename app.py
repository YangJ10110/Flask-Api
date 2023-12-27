from flask import Flask, request, jsonify
from flask_smorest import Api, Blueprint, abort
import json
import uuid
from db import stores, items

app = Flask(__name__)

@app.get('/')
def return_nothing():
    return "Nothing"

@app.get('/stores')
def get_stores():
    if not stores:
        abort(404, message="No stores yet")
    else:
        return "stores"


@app.get('/store/<int:store_id>')
def get_store(store_id):
    try:
        return f"ID: {store_id}"
    except TypeError:
        abort(404, message = "Store not found")

