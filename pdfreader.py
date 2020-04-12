import PyPDF2

pdfFileObj = open('C://Users//Ankita//Downloads//Resume_1.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

a=pageObj.extractText()
print(a)
with open('data.csv','w') as file:
    file.writelines(a)
pdfFileObj.close()