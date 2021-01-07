import PyPDF2
pdfFile = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
     pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('mihir123')
resultPdf = open('encrypted.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
