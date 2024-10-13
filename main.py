from flask import Flask, send_from_directory
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

PDF_DIR = os.path.join(os.path.dirname(__file__), 'pdfs')

# create a plug for the main page
@app.route('/')
def index():
    return 'Hello, World!'

# create a plug for the pdfs

@app.route('/pdfs')
def pdfs():
    return 'PDFs'


@app.route('/pdf/<filename>')
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)