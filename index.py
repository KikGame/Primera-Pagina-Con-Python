# Libraries
from flask import Flask
from flask import render_template

app = Flask(__name__)



# Home page
@app.route('/')
def home():
   return render_template("home.html")

# About page
@app.route('/about')
def about():
   return render_template("about.html")


# Debug page
if __name__ == '__main__':
   app.run(debug=True)