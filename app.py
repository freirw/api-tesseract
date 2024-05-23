from flask import Flask, request, jsonify, render_template
from database import SessionLocal, init_db
from models import Document
import pytesseract
from PIL import Image
from utils.extract import extract_data

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/upload')
def upload_file():
    if 'file' not in request.files:
        app.logger.debug('No file part')
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        app.logger.debug('No selected file')
        return jsonify({"error": "No selected file"}), 400

    try:
        image = Image.open(file.stream)
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)
        
        app.logger.debug('Raw extracted text: %s', text)  # Adicionando log do texto bruto

        extracted_data = extract_data(text)
        
        app.logger.debug('Extracted data: %s', extracted_data)
        return jsonify(extracted_data), 200
    except Exception as e:
        app.logger.error('Error processing file: %s', e)
        return jsonify({"error": str(e)}), 500

@app.get('/documents')
def list_documents():
    session = SessionLocal()
    documents = session.query(Document).all()
    return jsonify([{"id": doc.id, "filename": doc.filename, "content": doc.content} for doc in documents])

if __name__ == '__main__':
    app.run(debug=True)
