from __future__ import print_function
from flask import Flask, flash, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
import subprocess
import io
import os

blockname = "test1"
blastname = "test2"

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True


@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('index.html', title=title)



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


# check the file name and type, if correct, the files will be uploaded 
@app.route('/', methods=['POST'])

def upload_files():
        global blockname, blastname
        if request.files:
            file1 = request.files['file1']
            file2 = request.files['file2']
            blockname = file1.filename
            blastname = file2.filename
            if file1.filename == '':
                flash('No file part')
                print(" file must have a file name !")
                return redirect(request.url)
            # if file2.filename != "Blast_design":
            #     print ("Blast file name is wrong !")
            #     return redirect(request.url)
            # if file1.filename != "block_model":
            #     print ("Block file name is wrong !")
            #     return redirect(request.url)
            if not allowed_file(file1.filename):
                print("this file extension is not allowed !")
                print(file1.filename)
                return redirect(request.url)

            else:
                filename1 = secure_filename(file1.filename)
                filename2 = secure_filename(file2.filename)
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1.filename))
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2.filename))
                flash('files successfully uploaded and displayed')
                print(file1)
                print(file2)
                print(blockname)
                print(blastname)
                print(request.files)
                print('file saved')



                # str_output = run_program()
                # file_1 = "uploads/"+blockname
                # file_2 = "uploads/"+blastname
                # subprocess.run(["runfile.exe", "--blast_file", file_1, "--origin_file", file_2])
                return redirect(request.url)
               
               
                
           
    




#this is the function to run program

@app.route('/run_program',methods=['GET','POST'])
def run_program():
    file_1 = "uploads/"+blockname 
    file_2 = "uploads/"+blastname
    print(file_1)
    print(file_2)
    # subprocess.run(["runfile.exe", "--blast_file", file_1, "--origin_file", file_2])
    file_output ='test.txt'
    with open(file_output, "r") as file:
        content = file.read()
    return render_template("display.html", content=content)



# this section will display the content in txt file, please comment out the code above and try this one

# @app.route('/run_program',methods=['GET','POST'])
# def run_program():
#     file_output ='test.txt'
#     with open(file_output, "r") as file:
#         content = file.read()
#     return render_template("display.html", content=content)  


 # this is the function to download the files
@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                            filename=filename, as_attachment=False)  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
