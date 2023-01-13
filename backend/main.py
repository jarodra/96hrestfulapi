import os
from flask import Flask, request
from PIL import Image 

app = Flask(__name__)

# Allowed uploaded files definitions
UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

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
    # Search for the saved files and return it if it exists, else false
    folder = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)
    for file in os.listdir(folder):
        if file.rsplit('.', 1)[0] == str(stem):
            return file
    return False

def res_image(file_name):
    # Returns the height and width from a specified file
    img = Image.open(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER, file_name))
    width, height = img.size
    return [width, height]  

### Routing:
@app.route('/upload_image', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if there's a file
        if 'file' not in request.files:
            response = {'message': 'There\'s no file selected'} 
            return response, 400 
        # If there's no file selected the browser submits an empty file without a filename
        file = request.files['file']
        # Check if there's a non empty file
        if file.filename == '':
            response = {'message': 'No selected filename'}
            return response, 400 
        # Check if there's a file, with correct extension
        if file and allowed_file(file.filename):
            stem = str(count_uploaded_files())
            file_extension = get_file_extension(file.filename)
            file.save(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER, stem + '.' + file_extension))
            response = {'message': stem + ' is the number of the file'} 
            return response, 201
        response = {'message': 'Incorrect file extension'} 
        return response, 415

@app.route('/analyse_image/<int:id>', methods=['GET'])
def get_image(id):
    if find_files(id):
        height, width = res_image(find_files(id))
        response = {'height' : height, 
                    'width': width, 
                    'message': 'success'} 
        return response, 200
    response = {'message': 'The image does not exist'} 
    return response, 404

@app.route('/list_images', methods=['GET'])
def list_images():
    response = {'message': 'success'}
    return response, 200

# General error redirecting
@app.errorhandler(404)
def not_found(e):
    response = 'Resource not found'
    return response, 404


if __name__ == '__main__':
    app.run(debug=True)
