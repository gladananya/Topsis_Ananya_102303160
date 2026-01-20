from flask import Flask, request, render_template, send_file
import pandas as pd
import tempfile
import os
from topsis_ananya_102303160.topsis import run  # adjust import if needed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    weights = request.form['weights']
    impacts = request.form['impacts']

    df = pd.read_csv(file)
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')

    df.to_csv(temp.name, index=False)

    run(temp.name, weights, impacts, output_file.name)

    return send_file(output_file.name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
