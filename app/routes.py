from app import app
from flask import render_template, send_from_directory, jsonify, request
from .models import Value


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/service-worker.js', methods=['GET'])
def serve_service_worker():
    return send_from_directory(app.static_folder + '/..', 'service-worker.js')


@app.route('/add_value', methods=['POST'])
def add_value():
    if Value.add_value(request.get_json().get('value')):
        return jsonify(status='ok')
    return jsonify(status='bad request')


@app.route('/get_values', methods=['GET'])
def get_values():
    return jsonify(values=[value.serialize() for value in Value.get_values()])
