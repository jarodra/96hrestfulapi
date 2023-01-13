from flask import Flask
from flask import jsonify

def create_app(enviroment):
    app = Flask(__name__)
    return app

app = create_app()

app.route('/upload_image', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

app.route('/analyse_image/<id>', methods=['GET'])
def get_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/list_images', methods=['GET'])
def create_user():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)