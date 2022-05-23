from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/events_db'
mongo = PyMongo(app)


# Home page needs cprrect get for login or register page
@app.route('/')
def index():
    """returns home page"""
    return render_template('index.html')

# Route for User creation at register
# Comments:
#   Needs GET page that generates post form
@app.route('/users', methods=['POST'])
def create_user():
    """creates user page"""
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username and password and email:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {'username': username, 'password': hashed_password, 'email': email}
        )
        return "User Created Successfully"
    else:
        not_found()   
    
# Route for event creation for specific users
# Comments:
#   Needs GET page from user that generates post form
@app.route('/users/<user_id>/event_creation', methods=['POST'])
def create_event(user_id):
    """creates event for specified user"""
    nombre = request.json['nombre']
    location = request.json['location']
    fecha = request.json['fecha']
    if nombre and location and fecha:
        id = mongo.db.events.insert_one(
            {'nombre': nombre, 'location': location, 'fecha': fecha, 'user_id': user_id}
        )
        return "Event Created Successfully"
    else:
        not_found()


# Test Routes

@app.route('/map')
def map():
    """returns default map proximity template"""
    return render_template('map.html')

# Route for showing all events, needs testing for mongodb fetching events
@app.route('/event_list', methods=['GET'])
def event_list():
    """returns event list template"""
    list = mongo.db.events.find_all()
    response = json_util.dumps(list)
    return render_template('event_list.html', events = jsonify(response))

@app.route('/event/<id>')
def get_event(id):
    """returns event template"""
    event = mongo.db.events.find_one({'_id': id})
    return render_template('event.html', event = event)

# 404 page needs pretty html
@app.errorhandler(404)
def not_found(error=None):
    """returns 404 error page"""
    return "Recurso no encontrado" + request.url, 404

if __name__ == '__main__':
    app.run(debug=True)