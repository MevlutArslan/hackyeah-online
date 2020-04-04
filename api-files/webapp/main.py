import os
from flask import Flask, request, jsonify, render_template, redirect
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin
from Store import Store

app = Flask(__name__)

cred = credentials.Certificate('shop-safe-41c00-firebase-adminsdk-4j0q9-e631cbfa3b.json')
default_app = initialize_app(cred)
db = firestore.client()
store_ref = db.collection("Stores")

@app.route('/',methods=["GET","POST"])
def index():
    
    return render_template('index.html')

@app.route('/addStore',methods=["GET","POST"])
def addStore():
    if request.method == "POST":
        storename = request.form['storename']
        numberOfCashiers = int(request.form['numberOfCashiers'])
        openingHours = request.form["openingHours"]
        closingHours = request.form["closingHours"]
        numberOfWorkers = int(request.form["numberOfWorkers"])
        numberOfSecurityCameras = int(request.form["numberOfSecurityCameras"])
        # location = firestore.GeoPoint(request.form["latitude"],request.form["longtitude"])
        latitude = float(request.form["latitude"])
        longtitude = float(request.form['longtitude'])


        new_Store = Store(storename,numberOfCashiers,openingHours,closingHours,numberOfWorkers,numberOfSecurityCameras,latitude,longtitude)

        try:
            store_ref.document().set({
            'storename': new_Store._storename,
            'numberOfCashiers' : new_Store._numberOfCashiers,
            'openingHour' : new_Store._openingHour,
            'closingHour' : new_Store._closingHour,
            'numberOfEmployees' : new_Store._numberOfEmployees,
            'numberOfSecurityCameras' : new_Store._numberOfSecurityCameras,
            'location': firestore.GeoPoint(new_Store._latitude,new_Store._longtitude)
        })
        except:
            return "there was an error please try again "
        
        redirect('index.html')
    else:
        stores = []
    return render_template('addStores.html')

if __name__ == '__main__':
    app.run(debug=True)