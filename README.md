# Tamper Detection in Academic Credentials

This project is a lightweight web application for detecting tampering in academic documents like degree certificates, transcripts, and certifications. It uses PDF metadata analysis and visual layout matching to identify possible manipulations.

---

## 🚀 Features

* Extracts and analyzes PDF metadata for inconsistencies
* Compares uploaded documents with authentic templates using OpenCV
* Simple Flask-based web interface for uploading and scanning documents

---

## 🗂️ Project Structure

```
tamper_detection_app/
├── app.py                  # Flask app
├── static/
│   └── templates/          # Valid template images (e.g., valid_template.jpg)
├── uploads/                # Uploaded user files
├── templates/
│   └── index.html          # Web UI
├── utils/
│   ├── metadata_check.py   # PDF metadata analysis
│   └── template_match.py   # Image layout comparison
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tamper-detection-app.git
cd tamper-detection-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Files

* Place valid template images in `static/templates/`
* Upload test documents via the web UI

### 4. Run the Flask App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000/`

---

## 🧪 How It Works

* **PDFs**: Metadata is extracted (creation date, modification date, author, etc.). Suspicious edits are flagged.
* **Images**: Uploaded document images are compared to valid templates using OpenCV’s `matchTemplate`.

---

## 📝 Deliverables

* Source code (this repository)
* Technical report (PDF)
* Demo video (optional)
* Sample documents

---

## 📦 Dependencies

```
Flask
PyPDF2
opencv-python
pillow
numpy
```

---

