from flask import request, jsonify, render_template
from helpers import token_required
from car_site.models import db, User, Contact, contact_schema
from car_site import app

@app.route('/getdata')
def getdata():
    return User