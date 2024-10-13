from flask import Flask, send_from_directory
import os

app = Flask(__name__)

PDF_DIR = os.path.join(os.path.dirname(__file__), 'pdfs')

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)