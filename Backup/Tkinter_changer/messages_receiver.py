import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
import json




cred = credentials.Certificate("mycreds.json")
firebase_admin.initialize_app(cred)



db=firestore.client()

username="Abhay"
friend="Crush"
current_chat=db.collection(username).document(friend)

#docs = current_chat.stream()



doc_ref = db.collection(username).document(friend)

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')
    priny('Reload the page if you are facing ant issues')