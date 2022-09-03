import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore





cred = credentials.Certificate("mycreds.json")
firebase_admin.initialize_app(cred)



db=firestore.client()


username="Abhay"
message="Yaar, meri fatt ti hai, mein kya hi karu, so, if you ever sign up, you'll see this."

friend="Crush"

#used to create a collection in firestore, use it for usernames, and they can access only their user name collection, 
current_chat=db.collection(username).document(friend)
current_chat.set({'name':username, 'message': message})
