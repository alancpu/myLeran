
import requests
from bs4 import BeautifulSoup
import re

pathName = "C:\\Users\\meifeng\\Documents\\PycharmDocuments"

fileName = "pubmidTile.txt"

fileText = open(pathName+"\\"+fileName)

try:
   # allTheText = fileObject.read()
    for line in fileText:
        line = line.strip()
        #print(line)
        #m = re.match("growth",line)
        m = re.search("##",line)
        if m is not None:
            listLine = line.split("##")
            for subLine in listLine:
                print(subLine)
                res = requests.get(url='http://www.ncbi.nlm.nih.gov/pmc', params={'term': subLine})
                htmlRes = res.text
                soup = BeautifulSoup(htmlRes, 'html.parser')
                pmdId = soup.dd
                if pmdId is not None:
                    pmdIdStr = pmdId.string
                    print(subLine+"\t"+pmdIdStr)
                else:
                    print(subLine + "\t" + "None")
        else:
            print(line)
            res = requests.get(url='http://www.ncbi.nlm.nih.gov/pmc', params={ 'term': line})
            htmlRes = res.text
            soup = BeautifulSoup(htmlRes, 'html.parser')
            pmdId = soup.dd
            if pmdId is not None:
                pmdIdStr = pmdId.string
                print(line+"\t"+pmdIdStr)
            else:
                print(line+"\t"+"None")
        #print(line)
finally:
    fileText.close()




'''
res = requests.get(url='http://www.ncbi.nlm.nih.gov/pmc',params={'term':'Dominant-Activating, Germline Mutations in Phosphoinositide 3-Kinase p110δ Cause T Cell Senescence and Human Immunodeficiency '})

htmlRes = res.text

soup = BeautifulSoup(htmlRes, 'html.parser')


#print(soup.prettify())

print(soup.dd)
'''
