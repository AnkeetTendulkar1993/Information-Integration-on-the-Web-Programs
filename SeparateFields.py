'''
Created on Nov 2, 2016
Name: Ankeet Tendulkar
'''

import re
import csv

textFile1 = open('zagats.txt','r',encoding = 'utf-8')
f1 = textFile1.readlines()

csvFile = open("zagats.csv", "a+")
headNames = ["Name","Address","PhoneNumber","Type"]
c = csv.DictWriter(csvFile, fieldnames = headNames)
c.writeheader()
outerDict = {}
count  = 0
for eachLine in f1:
    line = eachLine.split()
    innerDict = {}
    i = len(line) - 1    
    rSt = re.search("\d{3}[-\/\s]\d{3}[-\/\s]\d{4}",eachLine)
    rE = re.search("\d{3}[-\/\s]\d{3}[-\/\s]\d{4}",eachLine)
    if rSt and rE:
        rStart = rSt.start()
        rEnd = rE.end()
        innerDict['number'] = eachLine[rStart:rEnd]
        innerDict['type'] = eachLine[rEnd+1:]
        endOfAddress = rStart
        i = 0
        while(i < endOfAddress):
            if(eachLine[i].isdigit()):  
                break 
            i += 1
        name = eachLine[0:i]
        address = eachLine[i:rStart]
        innerDict['name'] = name
        innerDict['address'] = address        
        outerDict[count] = innerDict
        c.writerow({'Name': innerDict['name'].strip(), 'Address': innerDict['address'].strip(), 'PhoneNumber':innerDict['number'].strip(), 'Type': innerDict['type'].strip()})
        count += 1 
             
print("Done")
  