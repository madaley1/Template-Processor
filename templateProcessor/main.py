from utils.openFile import openFile
from utils.getTemplatePoints import getTemplatePoints
def main(path):
    file = openFile(path)
    getTemplatePoints(file)