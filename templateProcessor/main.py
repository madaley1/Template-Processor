from utils.openFile import openFile
from utils.getTemplatePoints import getTemplatePoints
from utils.desiredValues import desiredValues
from utils.replaceText import replaceText

def main(path):
    file = openFile(path)
    matches = getTemplatePoints(file)
    values = desiredValues(matches)
    replaceText(file, values)
    