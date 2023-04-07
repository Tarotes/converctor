import os
import re
import docx
from io import StringIO
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import pandas as pd

def convert_to_txt(file_name):
    try:
        if file_name.endswith('.pdf'):
            with open(file_name, 'rb') as fh:
                text = extract_text(fh)
            output_string = StringIO()
            with open(file_name[:-4] + '.txt', 'w') as f:
                f.write(text)
        elif file_name.endswith('.docx'):
            doc = docx.Document(file_name)
            output_string = StringIO()
            for para in doc.paragraphs:
                output_string.write(para.text)
                output_string.write('\n')
            with open(file_name[:-5] + '.txt', 'w') as f:
                f.write(output_string.getvalue())
    except:
        pass

if __name__ == '__main__':
    for file_name in os.listdir('.'):
        convert_to_txt(file_name)
