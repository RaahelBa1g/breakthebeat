import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
from werkzeug.utils import secure_filename
import librosa
import subprocess 
import audioread

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
DOWNLOAD_FOLDER = "dowloads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = str(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))

            aud,sr = librosa.load(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            h_aud, p_aud = librosa.effects.hpss(aud)
            librosa.output.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename,".mp3"),p_aud,sr)
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''           

@app.route('/downloads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'],
                               filename)

if __name__=="__main__":
    app.run(debug=True)
    