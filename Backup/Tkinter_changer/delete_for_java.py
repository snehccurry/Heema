import pyrebase
from pyrebase import *


config={ 'apiKey': "AIzaSyD-DT8DKtXGaAvgeQF0t9J9SRxmu5nqbq4",
  'authDomain': "abhi-87f62.firebaseapp.com",
  'projectId': "abhi-87f62",
  'storageBucket': "abhi-87f62.appspot.com",
  'messagingSenderId': "415500621358",
  'appId': "1:415500621358:web:1a9fe7af2e7fb2609871bf",
  'measurementId': "G-385MYJL7BE",
  "databaseURL" : ""}


firebase=pyrebase.initialize_app(config)


auth=firebase.auth()
auth.sign_in_with_email_and_password


#database
db=firebase.database()


data={'age':23,'address':'LPU','employed':True, 'name': 'Abhay'}






db.push(data)	#used to create the data base/ push the data in the database