import pdfplumber
import re

fileurl1 = '.\\pdfs\\asamblea.pdf' 
fileurl2 = '.\\pdfs\\utp.pdf' 


def extractor(fileurl): 
    pdf = pdfplumber.open(fileurl)
    content = ''
    for page in pdf.pages:
        content = content + '\n' + page.extract_text()
    pdf.close()
    return content

def sentenceExtractor(content):
    oraciones = re.findall(r'\—[A-Z\sÑ\.\,ÁÉÍÓÚ]*([A-Z\sÑ\.\,ÁÉÍÓÚ][a-zA-Z\s\.áéíóúÁÉÍÓÚ\,\¿\?ñÑ0-9\'\"\:]*)', content)
    
    for oracion in oraciones:
        print(oraciones)

content = extractor(fileurl1)
oraciones = sentenceExtractor(content)
