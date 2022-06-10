#!/usr/bin/env python

from gtts import gTTS
import os, PyPDF2

#open the PDF file
PDFfile = open('input.pdf', 'rb')

PDFfilereader = PyPDF2.PdfFileReader(PDFfile)

#print the number of pages
print(PDFfilereader.numPages)

#provide the page number
pages = PDFfilereader.getPage(85)

#extracting the text in PDF file
inputText = pages.extractText()

#close the PDF file
PDFfile.close()
#mytext = 'this is a test, I am checking for clarity of voice and if you can tell this is missspellt'
  
def tts(inputText):

	output = gTTS(text=inputText, lang='en', tld='ie', slow=False)
  
	return output


tts(inputText).save("output.mp3")
  