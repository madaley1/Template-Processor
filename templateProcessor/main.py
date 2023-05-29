from utils.openFile import openFile
from utils.getTemplatePoints import getTemplatePoints
from utils.desiredValues import desiredValues
from utils.duplicateFile import duplicateFile
from utils.replaceText import replaceText

def main(path):
  file = openFile(path)
  matches = getTemplatePoints(file)
  values = desiredValues(matches)
  newPath = duplicateFile(file, path)
  #replace text may work, but isn't saving the pdf
  replaceText(path, newPath, values)
  print("Done!")