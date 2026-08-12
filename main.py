from flask import Flask, render_template
from flask_scss import Scss 
from flask_sqlalchemy import SQLAlchemy


#creating the website
app = Flask(__name__)

#creating the first page
#index is like the homepage
#we are building route for it 
#to create route use a decorator (use slah only coz its home page)
#the return here makes flask open up the index homepage from templates folder 
@app.route("/")
def index():
    return render_template("index.html")


#for running the app, debugger makes it update itself
#each page here is the HTML page, flask is the router

if __name__ in "__main__":
    app.run(debug=True)


#the templates folders hold each induvidual webpage
#static must be outside templates and holds css
#create index.html which is homepage use HTML:5 to create the boilerplate code

#in the index.html we will create a link to the css file in the static folder
#create the styles.scss and then click watch scss in the footer and it will create the styles.css file and the style.css.map in the static folder
#a different for css linking is used in the index.html file, it is different from the normal linking of css files, it is used to link the scss file to the html file
#here <link rel = "stylesheet" href={{url_for("static", filename = "style.css")}} /> is used.
#all css workings must be done in the styles.scss file and then it will be compiled to the style.css file which is linked to the index.html file