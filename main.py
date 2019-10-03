'''
@author: Blake Mullinax
Code created July 2019
'''
from flask import Flask, render_template, request

# set up flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result.html", methods=['GET', 'POST'])
def get_result():
	x = int(request.form['paramA'])
	y = int(request.form['paramB'])
	z = int(request.form['paramC'])
	calc1 = round((.32*x + .45*y + .23*z), 2)
	
	return render_template("result.html", result=calc1)
if __name__ == "__main__":
    app.run(debug=True)
