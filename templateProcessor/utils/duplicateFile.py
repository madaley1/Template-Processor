import shutil

def duplicateFile(file, path):
  title = path.split("/")[-1]
  print("duplicateFile", title)
  newTitle = input("Enter new title for " + title + ": ")
  print("newTitle", newTitle)
  newPath = path.replace(title, newTitle+".pdf")
  print(newPath)
  shutil.copyfile(path, newPath)
  return newPath