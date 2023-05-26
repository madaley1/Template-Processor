from py_modules.PyPDF2 import PdfReader
from pathlib import Path


def openFile(filePath):
  providedPath = Path(filePath)

  if providedPath.is_file() is False:
    raise ValueError("Please provide the path to an existing PDF file")

  return PdfReader(filePath)  
    