"""Prototype."""


from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

# Initialize flask
app = Flask(__name__, static_url_path='')

# get config
app.config.from_object('config')
app.secret_key = 'r��H�_���[��t'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/', methods=['POST', 'GET'])
def index():
	errormessage = ''

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if username == "admin" and password == "admin":
			session["admin_logged"] = True
			return redirect(url_for('admin_dashboard'))
		elif username == "user" and password == "user":
			session["user_logged"] = True
			return redirect(url_for('user_dashboard'))
		else:
			errormessage = 'Invalid username or password'

	return render_template('login.html', errormessage=errormessage)

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	if session.get('admin_logged', None):
		return render_template('admin_dashboard.html')
	else:
		return redirect(url_for('index'))

@app.route('/user/dashboard', methods=['GET'])
def user_dashboard():
	if session.get('user_logged', None):
		return render_template('user_dashboard.html')
	else:
		return redirect(url_for('index'))