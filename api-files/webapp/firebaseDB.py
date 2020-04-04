import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("shop-safe-41c00-firebase-adminsdk-4j0q9-6e4d32a62f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()