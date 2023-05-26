from py_modules.PyPDF2 import PdfReader
import re

def getTemplatePoints(file):
  pattern = "\[.*?\]"
  totalMatches = []
  for page in file.pages:
    text = page.extract_text()
    matches = re.findall(pattern, text)
    matchSet = set(matches)
    for match in matchSet:
      totalMatches.append(match)
  return set(totalMatches)