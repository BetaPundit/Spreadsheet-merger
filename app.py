import os
from flask import Flask, render_template, request, redirect, url_for
import excelSheetMerge
# from werkzeug import secure_filename

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['csv', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
      files = request.files['file[]']
      print(files)
    return render_template('upload.html')
    #   f.save(secure_filename(f.filename))
    #   if files and allowed_file(files.filename):
    #     filename = files.filename
    #     files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    #     excelSheetMerge.mergeFile(files)

    #     return redirect(url_for('uplaod', filename = files))
      
    #   else:
    #     return render_template('index.html', text='Error in file file input!<br>Please try uploading an image with supported formats:<br>(csv, xslx)')
      

if __name__ == '__main__':
    app.run(debug = True)