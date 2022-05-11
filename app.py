from flask import Flask, render_template
from data import Events
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.events_db
eventos = db.eventos

Events = Events()

@app.route('/')
def index():
    """returns home page"""
    return render_template('index.html')

@app.route('/map')
def map():
    """returns default map proximity template"""
    return render_template('map.html')

@app.route('/list')
def list():
    """returns event list template"""
    return render_template('event_list.html', events = Events)

@app.route('/event/<string:id>')
def event(id):
    """returns event template"""
    return render_template('event.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)