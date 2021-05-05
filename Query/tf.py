import os
from io import open
import nltk
import pandas as pd

def count_files():
    path = os.getcwd()
    number_files = sum([len(files) for r, d, files in os.walk(os.path.join(path,"Documentos p"))])
    return number_files

def readfiles(path):
    input_str=""
    with open(path,'r',encoding="utf-8") as file:
    	for lines in file.readlines():
    		input_str = input_str + lines
    cadena = str(input_str)

    return cadena.split()

def computeTF(wordDict, bow): #pendiente porque quizas no sirve
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count
    return tfDict

def computeTF_v2(diccionario, documento):
    for word in  documento:
       # print("pasada de diccionario TF: "+ str(i))
        diccionario[word]+=1

    return diccionario  # pendiente hasta ahora si sirve

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
    	if val > 0:
        	idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

number_files = count_files()

vocabulario = readfiles(os.path.join(os.getcwd(),"vocabulario","vocabulario.txt"))

documentos = []
for i in range(0,number_files):
    documentos.append(readfiles(os.path.join(os.getcwd(),"Documentos p",str(i+1)+".txt")))

diccionarios = []

for i in range(0,number_files):
    diccionarios.append(dict.fromkeys(vocabulario,0))

diccionarios_tf = []

for i in range(0,number_files):
    diccionarios_tf.append(computeTF_v2(diccionarios[i],documentos[i]))

tfs = pd.DataFrame(diccionarios_tf)

tfs.to_excel(os.path.join(os.getcwd(),"tf","tfs.xlsx"))

idfs = computeIDF(diccionarios_tf)

full_idfs = pd.DataFrame([idfs])  

full_idfs.to_excel(os.path.join(os.getcwd(),"idf","idfs.xlsx"))

tfidf = []

for i in range(0,number_files):
    tfidf.append(computeTFIDF(diccionarios_tf[i],idfs))

tfidf_full = pd.DataFrame(tfidf)

tfidf_full.to_excel(os.path.join(os.getcwd(),"tf_idf","tf_idf.xlsx"))

























'''vocabulario = readfiles(os.path.join(os.getcwd(),"vocabulario_temp.txt"))
documento_731 = readfiles(os.path.join(os.getcwd(),"1p.txt"))
documento_732 =readfiles(os.path.join(os.getcwd(),"2p.txt"))
diccionario_731 = dict.fromkeys(vocabulario,0)
diccionario_732 = dict.fromkeys(vocabulario,0)




for word in  documento_731:
	diccionario_731[word]+=1

for word in  documento_732:
	diccionario_732[word]+=1

print("-------------------------------------TF * ID -----------------------------------------------")
 
df = pd.DataFrame([diccionario_731,diccionario_732])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

print("------------------------------------- IDF -----------------------------------------------")
idfs = computeIDF([diccionario_731,diccionario_732])

df = pd.DataFrame([idfs])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)



tfidf_documento_731 = computeTFIDF(diccionario_731, idfs)
tfidf_documento_732 = computeTFIDF(diccionario_732, idfs)


print("-------------------------------------TF * ID -----------------------------------------------")
df = pd.DataFrame([tfidf_documento_731,tfidf_documento_732])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)'''




