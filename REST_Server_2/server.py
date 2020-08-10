
# Starte mit flask run

# Importieren der verwendeten Bibliotheken
from flask import Flask, json # Importieren der Flask Klasse. 
from decimal import Decimal
from flask import request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy #Datenbank
from sqlalchemy.sql import select  
import json

#CORS POLICY Notwendige Bibliotheken um Fehlermeldung zu umgehen. 
from flask import jsonify
from flask_cors import CORS

#Wichtige Initialisierung
app = Flask(__name__) 
CORS(app, resources={r'/*': {'origins': '*'}}) # Wichtig für CORS POLICY 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
#Position london weybridge 
#longitude = -0.46868189640700264
#latitude  = 51.35113755158258
location = [{"id": 1, "longitude": 123}, {"id": 2, "latitude": 123}]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)
# REST Anfrage entgegennehmen
@app.route('/loc', methods=['GET', 'POST']) # app.route gibt an bei welcher URL + POST Methode getriggert werden soll 
def get_loc():
  # =============== Aktualisieren der Position ===============
  if request.method == 'POST':
    print("Longitude: ", request.form['longitude'], "\n Latitude", request.form['latitude'])
    user = User(longitude = request.form['longitude'], latitude = request.form['latitude'])
    db.session.add(user)
    db.session.commit()
    return "Datenbankeintrag vorgenommen!"
  # =============== Abfrage der Position ===============
  else:
    #Letzte Wert ausgeben
    user = db.session.query(User).order_by(User.id.desc()).first()
    results = user     
    loc = [{"longitude": user.longitude, "latitude": user.latitude}]
    return jsonify(loc) # jsonify wichtig für CORS POLICY

if __name__ == '__main__':
  app.run()
























