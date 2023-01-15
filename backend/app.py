import os
from flask import Flask, request
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)

# File definitions
UPLOAD_FOLDER = './files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def allowed_file(file_name):
    # Check if the extensions are in the allowed file extensions
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_file_extension(file_name):
    # Return the file extension
    return file_name.rsplit('.', 1)[1].lower()


def count_uploaded_files():
    # Count the number of files inside files directory
    folder = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)
    return len(os.listdir(folder))


def find_files(stem):
    # Search for the saved files and return it if it exists, else None
    folder = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)
    for file in os.listdir(folder):
        if file.rsplit('.', 1)[0] == str(stem):
            return file


def res_image(file_name):
    # Returns the height and width from a specified file
    img = Image.open(os.path.join(os.path.dirname(
        __file__), UPLOAD_FOLDER, file_name))
    width, height = img.size
    return [width, height]

### Routing ###


@app.route('/upload_image', methods=['PUT'])
def upload_file():
    # Check if a file is selected
    if 'file' not in request.files:
        response = {'message': 'There\'s no file selected'}
        return response, 400
    file = request.files['file']
    # Check if a file is sent
    if not file:
        response = {'message': 'There\'s no file sent'}
        return response, 400
    # Check if there's a file, with correct extension
    if not allowed_file(file.filename):
        response = {'message': 'Incorrect file extension'}
        return response, 415
    # Read the file name, asign a name and save the file in the server
    stem = str(count_uploaded_files())
    file_extension = get_file_extension(file.filename)
    file.save(os.path.join(os.path.dirname(__file__),
              UPLOAD_FOLDER, stem + '.' + file_extension))
    response = {'message': stem + ' is the number of the file'}
    return response, 201


@app.route('/analyse_image/<int:id>', methods=['GET'])
def get_image(id):
    if find_files(id):
        height, width = res_image(find_files(id))
        response = {'height': height,
                    'width': width,
                    'message': 'success'}
        return response, 200
    response = {'message': 'The image does not exist'}
    return response, 404


@app.route('/list_images', methods=['GET'])
def list_images():
    folder = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)
    images = [images.rsplit('.', 1)[0] for images in os.listdir(folder)]

    return {'images': images, 'message': 'success'}, 200

# General error redirecting


@app.errorhandler(404)
def not_found(e):
    response = 'Resource not found'
    return response, 404


@app.errorhandler(405)
def not_found(e):
    response = 'Method Not Allowed'
    return response, 405


@app.errorhandler(413)
def not_found(e):
    response = 'The image was too large.'
    return response, 413


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
