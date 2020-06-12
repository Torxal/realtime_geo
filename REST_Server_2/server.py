
# Starte mit flask run

from flask import Flask, json
from decimal import Decimal
from flask import request
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
import json
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
#Position london weybridge 
#longitude = -0.46868189640700264
#latitude  = 51.35113755158258
companies = [{"id": 1, "longitude": 123}, {"id": 2, "latitude": 123}]
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/<longitude>/<latitude>')
def index(longitude, latitude):
    user = User(longitude=longitude, latitude=latitude)
    db.session.add(user)
    db.session.commit()
    return '<h1>Added New Position!</h1>'
@app.route('/loc', methods=['GET', 'POST'])
def get_companies():
  if request.method == 'POST':
    print("Longitude: ", request.form['longitude'], "\n Latitude", request.form['latitude'])
    user = User(longitude = request.form['longitude'], latitude = request.form['latitude'])
    db.session.add(user)
    db.session.commit()
    return "Datenbankeintrag vorgenommen!"
  else:
    #Letzte Wert ausgeben
    user = db.session.query(User).order_by(User.id.desc()).first()
    results = user     
    loc = [{"longitude": user.longitude, "latitude": user.latitude}]
    return json.dumps(loc)

if __name__ == '__main__':
  app.run()
























