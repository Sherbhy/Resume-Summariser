from flask import Flask, request, jsonify
import spacy
import PyPDF2

app = Flask(__name__)

# Define the path to your Spacy model folder
model_path = r"C:\Users\Surbhi Agarwal\Documents\My development projects\Resume Summariser\Resume-Summary-Tool\Backend - API and Spacy Model\FlaskDev\nlp_model"

# Load the Spacy model from the specified path
nlp_model = spacy.load(model_path)

def extract_text_from_pdf(pdf_file):
    # Function to extract text from PDF files
    text = ''
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

@app.route('/api/summarize', methods=['POST'])
def summarize_resume():
    # Check if a file was sent with the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if the file is a PDF
    if file.filename.endswith('.pdf'):
        # Extract text from the PDF file
        resume_text = extract_text_from_pdf(file)

        # Process the resume text with your SpaCy model
        doc = nlp_model(resume_text)

        # Extract entities and build the summary
        summary = []
        for ent in doc.ents:
            summary.append(f'{ent.label_.upper():{30}}- {ent.text}')

        return jsonify({'summary': summary}), 200

    else:
        return jsonify({'error': 'Unsupported file format. Please upload a PDF file'}), 400

if __name__ == '__main__':
    app.run(debug=True)
