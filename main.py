from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from db_setup import init_db

# set up flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiledata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "deloitte competition"

# set up database
db = SQLAlchemy(app)
init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result.html", methods=['GET', 'POST'])
def get_result():
	x = int(request.form['paramA'])
	y = int(request.form['paramB'])
	z = int(request.form['paramC'])
	calc1 = round((.32*x + .45*y + .23*z), 2)
	calc2 = round((.50*x + .14*y + .36*z), 2)
	calc3 = round((.25*x + .59*y + .16*z), 2)
	calc4 = round((.60*x + .25*y + .15*z), 2)
	
	return render_template("result.html",
	                        result=calc1,
							result2 = calc2,
							result3 = calc3,
							result4 = calc4)

if __name__ == "__main__":
    app.run(debug=True)
