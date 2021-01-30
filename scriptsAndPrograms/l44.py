import PyPDF2
import os
os.chdir('..\\textFile')

pdfFile = open('meetingminutes1.pdf', 'rb') # rb == read binary
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages

page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())

 