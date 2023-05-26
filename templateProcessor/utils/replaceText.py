from py_modules.PyPDF2 import PdfWriter
from pathlib import Path

def replaceText(filePath, values):
  print("replaceText")
  providedPath = Path(filePath)
  file = PdfWriter(filePath)

  for page in file.pages:
    text = page.extract_text()
    for value in values:
      text = text.replace(value["match"], value["value"])
    page.removeText()
    page.addText(text)
  print('replaced text')
  return
