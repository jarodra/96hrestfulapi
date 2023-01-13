from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_file():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/upload_image', methods=['POST'])
def post_upload():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/analyse_image/<int:id>', methods=['GET'])
def get_image(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/list_images', methods=['GET'])
def list_images():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
