from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set up flask app
app = Flask(__name__)
app.config.from_object(Config)

# set up database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
