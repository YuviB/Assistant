# Python Assitant for ASHS Students made by Yuvi

import pyrebase
import tkinter

# Authentication and Connection to Firebase

config = {
    "apiKey": "AIzaSyDK32ZP5bkJfjlihD7dvQoTzuzghPftqcI",
    "databaseURL":"https://assistant-cbb74-default-rtdb.firebaseio.com/",
    "authDomain": "assistant-cbb74.firebaseapp.com",
    "projectId": "assistant-cbb74",
    "storageBucket": "assistant-cbb74.appspot.com",
    "messagingSenderId": "628746129586",
    "appId": "1:628746129586:web:bb83d350335cac501eb9ab",
    "measurementId": "G-XV0KC4VN2B"
}

#Start connection to Firebase
firebase = pyrebase.initialize_app(config)

db=firebase.database()

data = {
"Test" : 1
}

db.child("Users").child("User1").set(data)

db.push(data)

auth=firebase.auth()

