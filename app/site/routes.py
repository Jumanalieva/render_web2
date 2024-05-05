from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('home.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/services')
def services():
    return render_template('/services')