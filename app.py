import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
uploaded_file_name = ""
UPLOAD_FOLDER = '/pycharm project/flask_try/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/output')
def output():
    # filename = request.args[file]
    filename = request.args.get('filename')
    from Text_processing import TextRankProject as tp
    tp.generate_summarized_op(filename)



@app.route('/')
def upload_file():
   return render_template("Index.html")


@app.route("/uploader", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('output',filename=file.filename))
    return redirect("output")
