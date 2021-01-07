
import PyPDF2 

def PDFrotate(origFileName, newFileName, rotation): 

	pdfFileObj = open(origFileName, 'rb') 
	
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

	pdfWriter = PyPDF2.PdfFileWriter() 
	
	for page in range(pdfReader.numPages): 

		
		pageObj = pdfReader.getPage(page) 
		pageObj.rotateClockwise(rotation) 

		
		pdfWriter.addPage(pageObj) 

	
	newFile = open(newFileName, 'wb') 
	
	
	pdfWriter.write(newFile) 

	
	pdfFileObj.close() 
	
	
	newFile.close() 
	

def main(): 

	
	origFileName = 'sample.pdf'
	newFileName = 'rotated.pdf'
	
	rotation = 180
	
	PDFrotate(origFileName, newFileName, rotation) 
	
if __name__ == "__main__": 
	 
	main() 
