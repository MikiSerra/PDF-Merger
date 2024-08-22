import PyPDF2 # import the PyPDF2 module
import sys # import the sys module because  we will be working with the command line
import os

merger = PyPDF2.PdfFileMerger() # create a PdfFileMerger object

for file in os.listdir(os.curdir): #
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write("merged.pdf")

