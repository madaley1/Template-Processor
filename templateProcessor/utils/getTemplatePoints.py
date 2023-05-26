from py_modules.PyPDF2 import PdfReader
import re

def getTemplatePoints(file):
  pattern = "/\[.*?\]/"
  for page in file.pages:
    text = page.extract_text()
    matches = re.findall(pattern, text)
    print(matches)