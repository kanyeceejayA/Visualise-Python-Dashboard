import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

UPLOAD_FOLDER = 'C:/Flask-Admin-Dashboard/static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/<filename>')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/static/img/photo1.png' 
    #+ filename
    return render_template('echo.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)