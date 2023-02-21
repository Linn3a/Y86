import subprocess

from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from forms import UploadForm
from flask import send_from_directory
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"


@app.route('/')
def hello_world():  # put application's code here
    return render_template("base.html")


app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')


@app.route('/upload', methods=["GET", "POST"])
def upload():
    form = UploadForm()
    success = 1
    receive = 0
    if form.validate_on_submit():
        f = form.file.data
        filename = "asum.yo"
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        bin_path = os.path.join("backend", "cpuTemp.exe")
        file_path = os.path.join("uploads", "asum.yo")
        output_path = "output.json"
        success = os.system(f"{bin_path} < {file_path} > {output_path}")
        receive = 1
    return render_template('upload.html', form=form, success=success, receive = receive)


@app.route('/display')
def display():
    return render_template('display.html')


@app.route('/file')
def file():
    try:
        return send_from_directory('', 'output.json')
    except Exception as e:
        return str(e)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
