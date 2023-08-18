from flask import Flask, jsonify, request
import os
import uuid

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    return jsonify({'hostname': os.uname().nodename})

@app.route('/author', methods=['GET'])
def get_author():

    author = os.getenv('AUTHOR', 'turnin-vv')
    return jsonify({'author': author})

@app.route('/id', methods=['GET'])
def get_id():
    unique_id = os.getenv('UID', str(uuid.uuid4()))
    return jsonify({'id': unique_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
