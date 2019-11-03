import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Fetch the service account key JSON file contents

def get_firestore_connection():
    cred = credentials.Certificate("megalodon-b5c06-firebase-adminsdk-k7emw-773b029ac5.json")

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://megalodon-b5c06.firebaseio.com/'
    })
    
    db = firestore.client()
    return db




