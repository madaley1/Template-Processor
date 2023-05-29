import shutil
from pathlib import Path

def duplicateFile(file, path):
  title = path.split("/")[-1]
  newTitle = input("Enter new title for " + title + ": ")
  newPath = path.replace(title, newTitle+".pdf")
  with open(newPath, "w") as newFile:
    pass
  newPathObject = Path(newPath)
  if newPathObject.is_file() is False:
    raise Exception("An Error Occurred while creating the new PDF file")
  
  return newPath