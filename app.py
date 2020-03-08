from flask import Flask
from flask import jsonify
from flask import request
import pymongo
from bson.json_util import dumps
app = Flask(__name__)
import bson
import json
from flask import Response
from flask import jsonify



@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"

@app.route("/consignments" , methods=['GET'])
def getAllConsignments():
    mongo = pymongo.MongoClient("mongodb+srv://sklogisticsadmin:Logistics!PWD@logisticsapp-sk-i4ikd.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = pymongo.database.Database(mongo, 'LogisticsApp')
    consignments = pymongo.collection.Collection(db, 'Consignment')
    #print(consignments)
    result = consignments.find();
    result = json.loads(dumps(result))
    resp = jsonify(result)
    resp.status_code = 200
    mongo.close()
    return resp

@app.route("/consignment", methods= ['GET'])
def getConsignment():
    mongo = pymongo.MongoClient("mongodb+srv://sklogisticsadmin:Logistics!PWD@logisticsapp-sk-i4ikd.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = pymongo.database.Database(mongo, 'LogisticsApp')
    consignments = pymongo.collection.Collection(db, 'Consignment')
    #print(consignments)
    result = consignments.find({"_id": bson.ObjectId(request.form['_id'])});
    result = json.loads(dumps(result))
    resp = jsonify(result)
    resp.status_code = 200
    mongo.close()
    return resp
