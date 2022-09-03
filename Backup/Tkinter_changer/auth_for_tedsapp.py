import pyrebase
from Heema import *
from pyrebase import *
config={ 'apiKey': "AIzaSyD-DT8DKtXGaAvgeQF0t9J9SRxmu5nqbq4",
  'authDomain': "abhi-87f62.firebaseapp.com",
  'projectId': "abhi-87f62",
  'storageBucket': "abhi-87f62.appspot.com",
  'messagingSenderId': "415500621358",
  'appId': "1:415500621358:web:1a9fe7af2e7fb2609871bf",
  'measurementId': "G-385MYJL7BE",
  "databaseURL" : "https://abhi-87f62-default-rtdb.asia-southeast1.firebasedatabase.app/"}



firebase=pyrebase.initialize_app(config)

#db=firebase.database()


auth=firebase.auth()

#storage=firebase.storage()




#authentication for the app
#login
#email=input("Enter your email id: ")
#password=input("Enter your password: ")

def login(email="",password=""):
  try:
    auth.sign_in_with_email_and_password(email,password)
    
    return "success"
    
  except:
    
    return "failed"
    



def sign_up_now(email,password):
  try:
    auth.create_user_with_email_and_password(email,password)
    
    return "success"
    
  except:
    messagebox(title="Sign UP", message="Sign up failed, check your internet connection")
    
    return "failed"
    







