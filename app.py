from __future__ import print_function
from flask import Flask, flash, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename

import io
import os

import numpy as np

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True


@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('index.html',
                           title=title)



# @app.route('/run',methods= ['GET'])
# def call_fx(blast,origin):
#     return blast, origin


path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')
# Make directory if "uploads" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# allowed extensions
ALLOWED_EXTENSIONS = {'csv'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        if request.files:
            file1 = request.files['file1']
            file2 = request.files['file2']
            if file1.filename == '':
                print(" file must have a file name !")
                return redirect(request.url)
            if not allowed_file(file1.filename):
                print("this file extension is not allowed !")
                print(file1.filename)
                return redirect(request.url)

            else:
                filename1 = secure_filename(file1.filename)
                filename2 = secure_filename(file2.filename)
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1.filename))
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2.filename))
            print(file1)
            print(file2)
            print(request.files)
            print('file saved')

            return redirect(request.url)
    return render_template('index.html')




# this is the function to download the files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
