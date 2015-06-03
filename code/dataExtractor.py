#Functions for extracting data

from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
from docx import Document #python-docx pacakage
import os
import codecs

################################
#pdf functions

def pdfToText(path):
	"""
	Args:
		path to pdf file

	Returns:
		a string of the pdf
	"""

	PDF = PdfFileReader(file(path, 'rb'))

	output = ""
	for page in PDF.pages:
	     output = output + page.extractText()

	return output

################################
#html functions

def urlToText(path):
	"""
	Args:
		path to html file

	Returns:
		a string of the html file
	"""
	with codecs.open(path, encoding='utf-8') as html:
		soup = BeautifulSoup(html)
	output = soup.get_text()

	return output


################################
#doc functions

def docToText(path):
	"""
	Turns docx file into a string.

	Note: it concatenates paragraphs and does not 
	distinguish between beginning and end of paragraphs

	Args:
		path to docx file

	Returns:
		a string of the docx file
	"""
	doc = Document(path)

	output = ""
	for paragraph in doc.paragraphs:
		output = output + paragraph.text

	return output



