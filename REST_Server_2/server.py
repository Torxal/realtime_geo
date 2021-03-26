# Starte mit flask run
from flask import Flask, json
from decimal import Decimal
from flask import request
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
import json
from sqlalchemy import text
from flask_cors import CORS
import sys
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
CORS(app)

#Position london weybridge 
#longitude = -0.46868189640700264
#latitude  = 51.35113755158258
#companies = [{"id": 1, "longitude": 123}, {"id": 2, "latitude": 123}]
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    time_exact = db.Column(db.String(10)) 
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self,longitude, latitude, time_exact):
        self.longitude = longitude
        self.latitude = latitude
        self.time_exact = time_exact

class Options(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  longitude = db.Column(db.String(50))
  latitude = db.Column(db.String(50))

  def __init__(self,longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

@app.route('/<longitude>/<latitude>')
def index(longitude, latitude, time_exact):
    loc = Location(longitude=longitude, latitude=latitude, time_exact = time_exact)
    db.session.add(loc)
    db.session.commit()
    return '<h1>Added New Position!</h1>'
@app.route('/loc', methods=['GET', 'POST'])
def get_location():
  if request.method == 'POST':
    print("Longitude: ", request.form['longitude'], "\n Latitude", request.form['latitude'], request.form['time_exact'])
    loc = Location(longitude = request.form['longitude'], latitude = request.form['latitude'], time_exact = request.form['time_exact'])
    db.session.add(loc)
    db.session.commit()
    return "Datenbankeintrag vorgenommen!"
  else:
    #Letzte Wert ausgeben
    loc = db.session.query(Location).order_by(Location.id.desc()).first()
    results = loc
    loc = [{"longitude": loc.longitude, "latitude": loc.latitude}]
    print("test")
    #return json.dumps(loc),201,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"http://127.0.0.1:5000"}
    return json.dumps(loc),201,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"*"}
@app.route('/loc_timeline', methods=['GET'])
def get_loc_timeline():
   stmt = select(Location).where(Location.longitude == '65')
   result = db.session.execute(stmt)
   for i in result.scalars():
     print(f"{i.longitude} {i.latitude}") 
   return f"{i.longitude} {i.latitude}"
@app.route('/delete_table', methods=['GET'])
def delete(): 
  db.session.execute(text("DELETE FROM Location"))
  db.session.commit()
  return "Tabelle gelöscht"
@app.route('/app_options', methods=['GET', 'POST'])
def options():
  if request.method == 'POST':
    #print("Longitude: ", request.form['longitude'], "\n Latitude", request.form['latitude'])
    #opt = Options(longitude = request.form['longitude'], latitude = request.form['latitude'])
    Options.query.get(1).longitude = request.form['longitude']
    Options.query.get(1).latitude = request.form['latitude']
    #db.session.add(opt)
    db.session.commit()
    print('Speichern der betrachteten Koordinaten', file=sys.stderr)
    print(request.form, file=sys.stderr)
    return  "test"
  else: 
    loc = db.session.query(Options).order_by(Options.id.desc()).first()
    results = loc
    loc = [{"longitude": loc.longitude, "latitude": loc.latitude}]
    print("Optioneninformationen erhalten")
    #return json.dumps(loc),201,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"http://127.0.0.1:5000"}
    return json.dumps(loc),201,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"*"}
if __name__ == '__main__':
  app.run(debug=True)
























