from firebase_admin import firestore, credentials, initialize_app

# initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
