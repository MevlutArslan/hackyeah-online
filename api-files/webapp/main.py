from flask import Flask, request, jsonify, render_template, redirect, jsonify
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin
from Store import Store

app = Flask(__name__)

cred = credentials.Certificate('shop-safe-41c00-firebase-adminsdk-4j0q9-e631cbfa3b.json')
default_app = initialize_app(cred)
db = firestore.client()
allStores = []
store_ref = db.collection("Stores")

@app.route('/',methods=["GET"])
def index():
    docs = store_ref.stream()
    _stores = [doc.to_dict() for doc in docs]
    _ids = [doc.id for doc in docs]
    print(_ids)
    return render_template('index.html',ids = _ids ,stores = _stores)

@app.route('/addStore',methods=["GET","POST"])
def addStore():
    if request.method == "POST":
        #get from the form
        # storename = request.form['storename']
        # numberOfCashiers = int(request.form['numberOfCashiers'])
        # openingHours = request.form["openingHours"]
        # closingHours = request.form["closingHours"]
        # numberOfWorkers = int(request.form["numberOfWorkers"])
        # numberOfSecurityCameras = int(request.form["numberOfSecurityCameras"])
        # latitude = float(request.form["latitude"])
        # longtitude = float(request.form['longtitude'])

        #local array
        # new_store = Store(storename,numberOfCashiers,openingHours,closingHours,numberOfWorkers,numberOfSecurityCameras,latitude,longtitude)
        
        #add to the database
        
        store_ref.document().set({
            'storename': request.form['storename'],
            'numberOfCashiers' : int(request.form['numberOfCashiers']),
            'openingHour' : request.form["openingHours"],
            'closingHour' : request.form["closingHours"],
            'numberOfEmployees' : int(request.form["numberOfWorkers"]),
            'numberOfSecurityCameras' :  int(request.form["numberOfSecurityCameras"]),
            'location': firestore.GeoPoint(latitude,longtitude),
            'que': new_store._que
        })
        redirect('index.html')
    else:
        pass
    return render_template('addStores.html')

@app.route('/store',methods=['GET','POST'])
def storeDetail():
    

    return render_template('store.html')

@app.route('/addToQue/<storeId>/<personID>',methods=["GET","POST"])
def addToQue(storeId,personID):
    que = (store_ref.document(storeId).get().to_dict()['que'])
    queLength = len(store_ref.document(storeId).get().to_dict()["que"])
    place = None
    if queLength > 0:
        place = (store_ref.document(storeId).get().to_dict()["que"][queLength-1]["place"])
    else:
        place = 0
    que.append({
        "place": place + 1,
        "person": personID,
    })
    store_ref.document(storeId).update({
        'que': que
    })
    # print(store_ref.document(storeId).get().to_dict()["que"][queLength-1]["place"])
    myPosition = 0
    # for store in _stores:

@app.route('/shiftQue/<storeId>', methods =["GET","POST"])
def shiftQue(storeId):
    que = (store_ref.document(storeId).get().to_dict()['que'])
    queLength = len(store_ref.document(storeId).get().to_dict()["que"])
    place = (store_ref.document(storeId).get().to_dict()["que"][queLength-1]["place"])
    que.pop(0)
    for i in range(queLength-1):
        que[i]["place"] -= 1
    store_ref.document(storeId).update({
        'que':que
    })
    myPosition = 0
    for x in que:
        if x["person"] == personID:
            myPosition = x["place"]

    return jsonify(myPosition)

@app.route('/getQuePlace/<storeId>/<personId>', methods=['GET','POST'])
def getQuePlace(storeId,personId):
    que = (store_ref.document(storeId).get().to_dict()['que'])
    queLength = len(store_ref.document(storeId).get().to_dict()["que"])
    place = (store_ref.document(storeId).get().to_dict()["que"][queLength-1]["place"])

    myPosition = 0

    for x in que:
        if x["person"] == personId:
            myPosition = x["place"]
    return jsonify(myPosition)
            

if __name__ == '__main__':
    app.run(debug=True)