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
    app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/', methods=['POST', 'GET'])
def index():
	errormessage = ''

	if session.get('admin_logged'): return redirect(url_for('admin_dashboard'))
	if session.get('user_logged'): return redirect(url_for('user_dashboard'))

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if username == "admin" and password == "admin":
			session["admin_logged"] = True
			session['user'] = 'admin'
			return redirect(url_for('admin_dashboard'))
		elif username == "user" and password == "user":
			session["user_logged"] = True
			session['user'] = 'user'
			return redirect(url_for('user_dashboard'))
		else:
			errormessage = 'Invalid username or password'

	return render_template('login.html', errormessage=errormessage)

@app.route('/logout/<type>')
def logout(type):
	if type == 'admin':
		session.pop('admin_logged')
	elif type == 'user':
		session.pop('user_logged')

	session.pop('user')

	return redirect(url_for('index'))

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	if session.get('admin_logged', None):
		return render_template('admin_dashboard.html', user=session['user'])
	else:
		return redirect(url_for('index'))

@app.route('/admin/user', methods=['GET'])
def admin_user():
	if session.get('admin_logged', None):
		return render_template('admin_user.html', user=session['user'])
	else:
		return redirect(url_for('index'))
		
@app.route('/admin/company', methods=['GET'])
def admin_company():
	if session.get('admin_logged', None):
		return render_template('admin_company.html', user=session['user'])
	else:
		return redirect(url_for('index'))
		
@app.route('/admin/project', methods=['GET'])
def admin_project():
	if session.get('admin_logged', None):
		return render_template('admin_project.html', user=session['user'])
	else:
		return redirect(url_for('index'))

@app.route('/admin/supplier', methods=['GET'])
def admin_supplier():
	if session.get('admin_logged', None):
		return render_template('admin_supplier.html', user=session['user'])
	else:
		return redirect(url_for('index'))
		
@app.route('/admin/customer', methods=['GET'])
def admin_customer():
	if session.get('admin_logged', None):
		return render_template('admin_customer.html', user=session['user'])
	else:
		return redirect(url_for('index'))
		
@app.route('/admin/cost-center', methods=['GET'])
def admin_cost_center():
	if session.get('admin_logged', None):
		return render_template('admin_cost_center.html', user=session['user'])
	else:
		return redirect(url_for('index'))
		
@app.route('/admin/operations', methods=['GET'])
def admin_operations():
	if session.get('admin_logged', None):
		return render_template('admin_operations.html', user=session['user'])
	else:
		return redirect(url_for('index'))

@app.route('/user/dashboard', methods=['GET'])
def user_dashboard():
	if session.get('user_logged', None):
		return render_template('user_dashboard.html', user=session['user'])
	else:
		return redirect(url_for('index'))