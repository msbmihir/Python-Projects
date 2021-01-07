import PyPDF2

ENCRYPTED_FILE_PATH = 'encrypted.pdf'

with open(ENCRYPTED_FILE_PATH, mode='rb') as f:        
    reader = PyPDF2.PdfFileReader(f)
    if reader.isEncrypted:
        reader.decrypt('mihir123')
        print(f"Number of page: {reader.getNumPages()}")
