from flask import Flask, escape, request, jsonify

from api.helpers.session import session_wrapper
from api.services.sessions import SessionService
from api.services.images import ImagesService

app = Flask(__name__)
app.services = {
    'session': SessionService(),
}


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/sessions', methods=['POST'])
def create_session():
    session_id = app.services['session'].create_session()
    return jsonify({'session_id': session_id})


@app.route('/sessions')
@session_wrapper()
def get_session():
    return jsonify(request.session.get().to_dict())


@app.route('/images/', methods=['GET'])
@session_wrapper()
def get_images():
    img_service = ImagesService(request.session)

    images = img_service.generate_images()
    return jsonify({'images': images})


@app.route('/images/', methods=['POST'])
@session_wrapper()
def save_images():
    data = request.json
    if not data.get('img_id'):
        return jsonify({'error': 'Missing img_id parameter in body'}), 400

    img_service = ImagesService(request.session)
    img_service.select_image(data['img_id'])

    return jsonify()
