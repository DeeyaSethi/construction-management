import secrets
from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename
 
#*** Backend operation

# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('static', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
 
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder='templates',static_folder='static')
#, template_folder='SafetyOfWOrkersFinal/templateFiles', static_folder='SafetyOfWOrkersFinal/staticFiles')
# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# directory_path = 'construction-management/static/SafetystaticFiles/uploads'
# permissions = os.stat(directory_path).st_mode

# Define secret key to enable session
# app.secret_key = 'This is your secret key to utilize session in Flask'
app.secret_key = secrets.token_hex(16)
 
@app.route('/')
def index():
    return render_template('Index.html')
    # return render_template('index_upload_and_show_data.html')

@app.route('/TrackProgress/progress.html')
def progress():
    return render_template('TrackProgress/progress.html')

@app.route('/InventoryMgmt/inventory_file.html')
def inventory():
    return render_template('InventoryMgmt/inventory_file.html')

@app.route('/ReportCorruption/rc.html')
def reportCorruption():
    return render_template('ReportCorruption/rc.html')

# @app.route('/InventoryMgmt/inventory_file.html')
# def progress():
#     return render_template('InventoryMgmt/inventory_file.html')

@app.route('/SafetyOfWOrkersFinal/templateFiles/index_upload_and_show_data.html')
def uploadFile():
        return render_template('SafetytemplateFiles/index_upload_and_show_data.html')

@app.route('/', methods = ("POST", "GET"))
def upload():
    if request.method == 'POST':
        # Upload file flask
        uploaded_img = request.files['uploaded-file']
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        if os.path.exists(app.config['UPLOAD_FOLDER']):
            if os.access(app.config['UPLOAD_FOLDER'], os.W_OK):
                print(f"The directory is writable.")
            else:
                print(f"The directory is not writable.")
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        print("Uploaded file:", img_filename)
        print("UPLOAD_FOLDER:", app.config['UPLOAD_FOLDER'])
        new_permissions = 0o700

        # Use os.chmod() to change permissions
        os.chmod(app.config['UPLOAD_FOLDER'], new_permissions)
        print(f'Permissions changed')

        # Upload file to database (defined uploaded folder in static path)
        # with open(UPLOAD_FOLDER, 'w+'):
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER']), img_filename)
        # print(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

    return render_template('SafetytemplateFiles/index_upload_and_show_data_page2.html')
     
@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    img_file_path = session.get('uploaded_img_file_path', None)
    # Display image in Flask application web page
    return render_template('SafetytemplateFiles/show_image.html', user_image = img_file_path)
 
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug = True)