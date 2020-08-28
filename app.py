from flask import Flask, render_template, request, redirect,session
import pyrebase

app = Flask(__name__)
app.secret_key="secert"
# firebase
config = {
    "apiKey": "AIzaSyC7cyZHHcqFfSmhr7oLC2h-uoF3V_KoEQU",
    "authDomain": "chat-9e9d5.firebaseapp.com",
    "databaseURL": "https://chat-9e9d5.firebaseio.com",
    "projectId": "chat-9e9d5",
    "storageBucket": "chat-9e9d5.appspot.com",
    "messagingSenderId": "613198926114",
    "appId": "1:613198926114:web:3e9679d09cd48f0425557b"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/task", methods=['POST'])
def inputData():

    # getting userInput
    nameOfTask = request.form.get("nameOfTask")

    # sending data into db
    db.child("todoList").push(nameOfTask)

    # now we will get data from db to display on index page
    taskFromDb = db.child("todoList").get()
    taskName = taskFromDb.val()
    
    session['key'] = taskName
    key = ""
    value = ""
    for k, v in taskName.items():
        key = k
        value = v

    # sending data back to page along with the list of tasks
    return render_template("index.html", taskName=taskName.items())
    return redirect(url_for('/task/deleteAll/'))


# Using this method all the tasks will be deleted
@app.route('/task/deleteAll/')
def deleteTask():
# removing data from db
   db.child().remove()
   return render_template("index.html")
  
    
