'''
Name: Ankeet Tendulkar
CSCI 548 Assignment 2
'''

import nltk

file = open('inputRawData.txt','r')
f = file.readlines()
outputFile = open('cleanedTestingData.txt', 'w')

# Identifying sentences from raw text
sentence = ""
for eachLine in f:
    cleanLine = eachLine.replace(',','').replace('(','').replace(')','').replace('[','').replace(']','').replace('#','').replace(':','').replace(';','').replace('-','')
    newCleanLine = cleanLine.split()
    for word in newCleanLine:
        if word[len(word) - 1] != '.':
            sentence += " " + word
        else:
            sentence += " " + word[0:len(word) - 1]
            outputFile.write(sentence + "\n")
            sentence = ""
outputFile.close() 
print("Cleaned raw data....")           
    
file = open('cleanedTestingData.txt','r')
f = file.readlines()

listOuter = []

# Identifying the POS for each sentence
for eachLine in f:
    listForPOS = []
    temp = eachLine.split()
    for word in temp:
        listForPOS.append(word)
    taggedData = nltk.pos_tag(listForPOS)    
    for i in range(0, len(taggedData)):
        listInner = []
        listInner.append("word=" + taggedData[i][0])
        listInner.append("pos=" + taggedData[i][1])
        listOuter.append(listInner)
    listOuter.append([])
      
print("Identified POS Feature....")

# Identifying the rest of the features
article = ['a','an','the','A','An','The']
print("Identifying features....")    
for i in range(0, len(listOuter)):
    if(len(listOuter[i]) != 0):
        flag = ""
        listOuter[i].append("first=" + listOuter[i][0][5:][0]) #firstLetter
        listOuter[i].append("last=" + listOuter[i][0][len(listOuter[i][0])-1]) #lastLetter
        # If word begins with capital letter
        if(str(listOuter[i][0][5:][0]).isupper()):
            listOuter[i].append("capital=Y")
        else:
            listOuter[i].append('capital=N')
        # If the word is a number
        if(listOuter[i][0][5:].isdigit()):
            listOuter[i].append('number=Y')
        else:
            listOuter[i].append('number=N')
        # If word is an article
        if listOuter[i][0][5:] in article:
            listOuter[i].append('article=Y')
        else:
            listOuter[i].append('article=N')
        # If the word is beginning of sentence
        if i == 0:
            listOuter[i].append('beginning=Y')
            flag = "__BOS__"
        elif listOuter[i-1] == []:
            listOuter[i].append('beginning=Y')
            flag = "__BOS__"
        else:
            listOuter[i].append('beginning=N')    
        # If the word is end of sentence
        if len(listOuter[i+1]) == 0:
            listOuter[i].append('end=Y')
            flag = "__EOS__"
        else:
            listOuter[i].append('end=N')
        if flag != "":
            listOuter[i].append(flag)

# Storing data in the output file        
print("Writing to output file......")
outputFile = open('testing.txt', 'w')
for outer in listOuter:
    for inner in outer:
        outputFile.write(inner + "\t")
    outputFile.write("\n")    
outputFile.close()
print("Finished writing to output file...")     