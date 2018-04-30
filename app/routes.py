from app import app
from flask import render_template, send_from_directory


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/service-worker.js', methods=['GET'])
def serve_service_worker():
    return send_from_directory(app.static_folder + '/..', 'service-worker.js')
