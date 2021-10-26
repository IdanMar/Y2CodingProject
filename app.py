from flask import Flask, render_template, request, redirect,url_for
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iasas-food-is-good'

# TODO: Add all of the routes you want below this line!

@app.route("/login", methods = ['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if get_user_by_mail(request.form['email']) != None and request.form['password'] == get_user_by_mail(request.form['email']).word:
			return redirect(url_for('ads'))
		return render_template('login.html')

@app.route("/aboutus")
def aboutus():
	return render_template('aboutus.html')

@app.route("/donations")
def paypal():
	return render_template('paypal.html')



@app.route("/ads")
def ads():
	return render_template('ads.html')

@app.route("/signupsub", methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template("homepage.html")
	else:
		add_user(
			name=request.form['signupname'],
			email=request.form['signupemail'],
			word=request.form['signupword'],
			donate = 0
			 )

		return redirect(url_for('ads'))

@app.route("/")
def index():
	return render_template("index.html")

# @app.route("/")
# def index():
# 	return render_template("homepage.html")


if __name__ == "__main__":
	app.run(host="localhost", port=8080, debug=True)