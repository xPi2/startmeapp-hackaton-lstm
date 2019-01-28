import os
import re
import time
from random import randint, choice

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from utils import GetLatLon, get_antonyms, get_synonyms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
port = int(os.getenv('VCAP_APP_PORT', 5000))
index_add_counter = 0


@app.route('/')
def index():
    global index_add_counter
    return render_template('index.html')

@app.route('/char')
def char():
    global index_add_counter
    return render_template('char.html')


@app.route('/post/<value>', methods=['POST'])
def post(value):
    global index_add_counter
    index_add_counter += 1
    val = (request.get_json()['num_object'])
    image = (request.get_json()['objects'])
    if val != 0:
        send_to_front(val)
    # TO DO Create send to socket for value of detections.
    return str(index_add_counter)

@app.route('/clean/', methods=['POST'])
def clean():
    clean_front()
    return str("CLEAN!")

@socketio.on('clean', namespace='/app')
def clean_front():
    emit('graph_data', {
        'date': time.strftime("%a %m/%d/%Y"),
        'time': time.strftime("%H:%M:%S"),
        'value': 1032010
    }, namespace='/app', broadcast=True)


@socketio.on('message', namespace='/app')
def send_to_front(value):
    emit('graph_data', {
        'date': time.strftime("%a %m/%d/%Y"),
        'time': time.strftime("%H:%M:%S"),
        'value': value
    }, namespace='/app', broadcast=True)


@socketio.on('connect', namespace='/app')
def connect():
    emit('check_connection', {'data': 'Connected'})



@socketio.on('message', namespace='/app')
def message():
    emit('graph_data', {
        'date': time.strftime("%a %m/%d/%Y"),
        'time': time.strftime("%H:%M:%S"),
        'value': 0
    })

genLatLon = GetLatLon('static/countries-capitals.json')


@socketio.on('google_map', namespace='/app')
def google_map():
    emit('map_data', genLatLon.__next__())


@socketio.on('input_broadcast_event', namespace='/app')
def word_cloud_broadcast(msg):
    emit('input_broadcast', {'data': msg['data']})


@socketio.on('input_event', namespace='/app')
def word_cloud(msg):
    print(msg)
    if len(msg['data'].split()) == 1:
        limit = 20  # Not more than `limit` antonyms and synonyms
        antonyms = get_antonyms(msg['data'], limit)
        synonyms = get_synonyms(msg['data'], limit)
        words = list(map(lambda x: {'text': x, 'flag': 1, 'size': randint(10, 50)}, synonyms))
        words.extend(list(map(lambda x: {'text': x, 'size': randint(10, 50)}, antonyms)))
    else:
        words = list(map(lambda x: {'text': x, 'flag': choice([0, 1]), 'size': randint(10, 50)},
                         re.findall("[a-zA-Z\d]+", msg['data'])))
    emit('input', {'words': words})


@socketio.on('input_broadcast_event', namespace='/app')
def test_message(msg):
    emit('input_broadcast', {'data': msg['data']}, broadcast=True)


@socketio.on('disconnect', namespace='/app')
def disconnect():
    print('Client disconnected!')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=port)
