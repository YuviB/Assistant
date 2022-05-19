# Python Assitant for ASHS Students made by Yuvi
#Imports
import pyrebase
import tkinter


#Config and Information for Connection to firebase
config = {
   "apiKey": "AIzaSyAJrhmQCb84w34Nla-e98Xz-a23ujG6gi8",
 "authDomain":  "atlastest-16c41.firebaseapp.com",
  "databaseURL": "https://atlastest-16c41-default-rtdb.firebaseio.com",
  "projectId": "atlastest-16c41",
  "storageBucket": "atlastest-16c41.appspot.com",
  "messagingSenderId": "314558802294",
 " appId": "1:314558802294:web:3277a14206e43160507257",
 " measurementId": "G-W0LPMQ0X64"
}

#Start Up Pyrebase to communicate to Firebase
firebase = pyrebase.initialize_app(config)

db=firebase.database()

data = {"Age": 21, "Name": "James", "Pet": "Dog" }

db.child("Users").child("User1").set(data)

db.push(data)


auth=firebase.auth()

#Variables
global email
global password
global UserName
global inputPassword





#Functions




def lengthCheck():
        inputPassword = 0
        if len(inputPassword) > 6:
            print("Please enter a password with 6 characters or more")
            CreateAccount()
        else:
            password = inputPassword
            auth.create_user_with_email_and_password(email, password)
            global confirm
            confirm = 0
            print("Account Created, Redirecting to Sign Up")
            SignIN()



#SignIn Function - This is the fucntion the user is rediricted if they have an exisitng account
def SignIN():
 emaillogin = input("Enter your email")
 passwordlogin = input("Enter your Password")

 auth.sign_in_with_email_and_password(emaillogin, passwordlogin)

 if auth.sign_in_with_email_and_password(emaillogin, passwordlogin):

  print("Welcome" + UserName)
 else:
  print("fail")
pass



#Intro - Sign in Prompt
def SignInCheck():
 progress = input("Would You Like to Sign in? (Y/N)")

 if progress == "Y" or "y":
  SignIN()


  pass


 elif progress == "N" or "n":
  print("Okay Goodbye")

 else:
  print("Please Enter Y or N")


 pass



#Creat Accounts - This is the rediretced function if User selects new user
def CreateAccount():

    UserName = input("Enter your first name ")
    email = input("Enter Email ")
    inputPassword = input("Please Enter a Password with 6 or more characters ")
    print("Your Password is ", len(inputPassword), "Characters Long")

    print()
    if (len(inputPassword) >=6):
        password = inputPassword
        auth.create_user_with_email_and_password(email, password)
        print("Sucsess")
    else:
        ("Print Invalid Password Length")
        CreateAccount()


















pass








#Intro - First Prompt to User in Form of Text
print("Hello, Welcome to (Yuvis Test) are you a new user or an existing user? ")

NewUser = input("(N) New User, (E) Existing User\n")

if NewUser == "N": #Prompts user for Sign up or Login
    CreateAccount()

elif NewUser == "E":
    SignIN()




