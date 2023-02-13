from flask import Flask,request,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager,jwt_required,create_access_token 
import requests
import os 

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = '123456789'
jwt = JWTManager(app)

if os.path.isfile("env.py"):
    import env

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/weather', methods=['GET'])
@jwt_required()
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    API_KEY = os.environ.get("SECRET")
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

    response = requests.get(url)
    data = response.json()
    return jsonify(data), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

if __name__ == '__main__':
    app.run(debug=True)

