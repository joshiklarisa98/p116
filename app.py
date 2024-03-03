# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Klarisa" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    return "This is the father webpage"

# define the route to mother webpage
@app.route("/mother")
def mother():
    return "This is the mother webpage"

# define the route to friends webpage
@app.route("/friends")
def friends():
    return "This is the friends webpage"

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)