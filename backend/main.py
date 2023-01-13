from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Allowed uploaded files definitions
UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def allowed_file(filename):
    # Check if the extensions are in the allowed file extensions
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    # Return the file extension
    return filename.rsplit('.', 1)[1].lower()

def count_uploaded_files():
    # Count the number of files inside files directory
    folder = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)
    return len(os.listdir(folder))

### Routing:
@app.route('/', methods=['GET'])
def index():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/upload_image', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if there's a file
        if 'file' not in request.files:
            response = {'message': 'There\'s no file part'} #!!! Add status codes
            return jsonify(response)
        # If there's no file selected the browser submits an empty file without a filename
        file = request.files['file']
        # Check if there's a non empty file
        if file.filename == '':
            response = {'message': 'No selected file'} #!!! Add status codes
            return jsonify(response)
        # Check if there's a file, with correct extension
        if file and allowed_file(file.filename):
            file_name = str(count_uploaded_files())
            file_extension = get_file_extension(file.filename)
            file.save(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER, file_name + '.' + file_extension))
            response = {'message': file_name + ' is the number of the file'} #!!! Add status codes
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
