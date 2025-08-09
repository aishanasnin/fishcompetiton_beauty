import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from model import fish_analysis

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    images = request.files.getlist('images')
    names = request.form.getlist('names')
    saved_paths = []

    for f in images:
        if f and f.filename:
            filename = secure_filename(f.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(path):
                filename = f"{base}_{counter}{ext}"
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                counter += 1

            f.save(path)
            saved_paths.append(path)

    # Run analysis
    results = fish_analysis.analyze(saved_paths, names)
    winner_index = max(range(len(results)), key=lambda i: results[i]['total_score']) if results else None

    if winner_index is not None:
        winner_name = results[winner_index]['name']
        return redirect(url_for('certificate', winner_name=winner_name))
    else:
        return "No competitors were provided."

@app.route('/certificate/<winner_name>')
def certificate(winner_name):
    return render_template('certificate.html', name=winner_name)

if __name__ == '__main__':
    app.run(debug=True)
