import PyPDF2

def extract_metadata(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            info = reader.metadata
            return info
    except Exception as e:
        return {"Error": str(e)}

def analyze_metadata(info):
    red_flags = []
    if not info or isinstance(info, dict) and "Error" in info:
        red_flags.append("Could not extract metadata.")
        return red_flags

    creation_date = info.get('/CreationDate', '')
    mod_date = info.get('/ModDate', '')
    author = info.get('/Author', '')
    producer = info.get('/Producer', '')

    if creation_date and mod_date and creation_date != mod_date:
        red_flags.append("Mismatch between CreationDate and ModDate.")

    if not author or author.lower() in ['anonymous', '']:
        red_flags.append("Author metadata is missing or invalid.")

    if producer and any(tool in producer.lower() for tool in ['word', 'photoshop', 'libreoffice']):
        red_flags.append(f"Suspicious software used: {producer}")

    return red_flags
