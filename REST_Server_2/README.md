Kompilierung einrichten: 
Befehl: set-executionpolicy Unrestricted 
Eingabe nach Frage => Für alle
1. Im Ordner REST_SERVER_2 eingeben: env\Scripts\activate
2. set FLASK_APP=server.py
3. flask run
Datenbank neu aufsetzen
1. Eingabe python 
2. from server import db 
3. db.create_all()
4. quit()
