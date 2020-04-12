import docx
import os
os.chdir('C://Users//Ankita//Downloads')
doc: object = docx.Document('Resume_1.docx')
i=0
l=[]
while True:
    try:
        x = doc.paragraphs[i].text
        l.append(x)
        i = i + 1
    except:
        break
os.chdir('C://Users//Ankita//.PyCharmCE2019.1//config//Scratches')
with open('data1.xlsx','w') as file:
    file.writelines(l)
