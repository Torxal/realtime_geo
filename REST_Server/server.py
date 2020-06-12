from flask import Flask, json

companies = [{"id": 1, "longitude": "-0.46868189640700264"}, {"id": 2, "latitude": "51.35113755158258"}]

api = Flask(__name__)

@api.route('/loc', methods=['GET'])
def get_companies():
  return json.dumps(companies)

if __name__ == '__main__':
    api.run()