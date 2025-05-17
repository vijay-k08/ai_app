from flask import Flask, render_template, request
from utils.metadata_check import extract_metadata, analyze_metadata
from utils.template_match import compare_templates
import os

UPLOAD_FOLDER = 'uploads'
TEMPLATE_IMAGE = 'static/templates/valid_template.jpg'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    metadata_issues = []
    template_result = ""

    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Check file type
            if file.filename.endswith('.pdf'):
                metadata = extract_metadata(file_path)
                metadata_issues = analyze_metadata(metadata)

            elif file.filename.endswith(('.jpg', '.png')):
                template_result = compare_templates(file_path, TEMPLATE_IMAGE)

    return render_template("index.html",
                           metadata_issues=metadata_issues,
                           template_result=template_result)

if __name__ == '__main__':
    app.run(debug=True)
