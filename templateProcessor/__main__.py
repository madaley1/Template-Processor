import sys
from main import main

numElements = len(sys.argv) - 1

if(numElements > 1):
  raise ValueError("Please only provide one file path at a time")
elif(numElements <= 0):
  raise Exception("Please provide the path to the PDF you wish to process")
else:
  main(sys.argv[1])