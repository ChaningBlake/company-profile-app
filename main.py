from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# set up flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiledata.db'
app.secret_key = "deloitte competition"

# set up database
db = SQLAlchemy(app)

from app import routes, models


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result.html", methods=['GET', 'POST'])
def get_result():
	x = int(request.form['paramA'])
	y = int(request.form['paramB'])
	z = int(request.form['paramC'])
	calculation = x + y + z
	
	return render_template("result.html",
	                        result=calculation)

if __name__ == "__main__":
    app.run(debug=True)
