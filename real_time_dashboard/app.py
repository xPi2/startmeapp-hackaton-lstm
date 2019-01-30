import os
import re
import time
from random import randint, choice

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
port = int(os.getenv('VCAP_APP_PORT', 5000))
index_add_counter = 0


@app.route('/')
def index():
    global index_add_counter
    return render_template('char.html')

@app.route('/char')
def char():
    global index_add_counter
    return render_template('char.html')


@app.route('/post/<value>', methods=['POST'])
def post(value):
    global index_add_counter
    index_add_counter += 1
    val = (request.get_json()['num_objects'])
    image = (request.get_json()['frame'])
    send_to_front(val, image)
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



if __name__ == '__main__':
    socketio.run(app, debug=True, port=port)
