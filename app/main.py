from functools import wraps

from flask import redirect, render_template, request, session, url_for
from flask_login import login_user

from app import app, dao, login, models
from app.models import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/inner-page')
def inner_page():
    return render_template('inner-page.html')

@app.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.validate_user(username=username, password=password)
        if user:
            login_user(user=user)
    return redirect('/admin')

@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)

# @app.route('/model')
# def model():
#     models.db.create_all()
#     return 'successful'

if __name__ == "__main__":
    app.run(debug=True)
