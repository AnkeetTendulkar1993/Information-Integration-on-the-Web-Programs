'''
Name: Ankeet Tendulkar
Homework 3
'''

from bs4 import BeautifulSoup
import urllib
from urllib.request import Request,urlopen
import os
import fnmatch
 
# Open a file and create Beautiful Soup object  
def openFile(fpath): 
    global jsonList
    jsonList = []
    webpage = open(fpath,'r')
    global soup
    soup = BeautifulSoup(webpage,"html.parser")

# Write the data in JSON Format 
def writeInJSONFormat(ky,val):
    pairkv = "\"" + ky + "\"" + ":" + "\"" + val + "\""
    jsonList.append(pairkv)
    return    
 
# Extract relevant data from each webpage       
def process():
    try:
        q1 = soup.find("meta",{"property":"og:url"}).renderContents()
        s = str(q1.strip())
        w = s.index("https://www.udemy.com/")
        s1 = s[w:].encode('utf-8')
        s2 = s1.split()[0]
        print("URL = {}".format(str(s2)[2:len(s2) + 1]))
        k = "URL"
        v = str(s2)[2:len(s2)+1]
        #print(v)
        if v != "":
            writeInJSONFormat(k,v)
    except:
        print("No URL")
    
    try:
        q1 = soup.find("a",{"class":"thb-n prox ud-popup"}).renderContents()
        q2 = str(q1.strip())
        q3 = q2.replace("\\n","").encode('utf-8')
        print("Instructor = {}".format(str(q3)[4:len(q3)+1]))
        k = "Instructor"
        v = str(str(q3)[4:len(q3)+1])
        if v != "":
            writeInJSONFormat(k,v)
    except:
        print("No Instructor")
    
    try:
        q1 = soup.find("a",{"class":"cd-ca"}).renderContents()
        q2 = str(q1.strip())
        q3 = q2.replace("\\n","").encode('utf-8')
        print("Domain = {}".format(str(q3)[4:len(q3)+1]))
        k = "Domain"
        v = str(str(q3)[4:len(q3)+1])
        if v != "":
            writeInJSONFormat(k,v)
    except:
        print("No Domain")
    
    try:
        q1 = soup.find("h1",{"class":"course-title","data-purpose":"course-title"}).renderContents()
        q2 = str(q1.strip())
        q3 = q2.replace("\\n","").encode('utf-8')
        print("Title = {}".format(str(q3)[4:len(q3)+1]))
        k = "Title"
        v = str(str(q3)[4:len(q3)+1])
        if v != "":
            writeInJSONFormat(k,v)
    except:
        print("No Title")
        
    try: 
        for sec in soup.findAll("span",{"class":"current-price"}):
            r = str(sec.renderContents().strip()).encode('utf-8')
            print("Original Price = {}".format(str(str(r)[4:len(r)+1]))) 
        k = "Original Price"
        v = str(str(r)[4:len(r)+1])
        if v != "":
            writeInJSONFormat(k,v)  
    except:
        print("No Current Price")
    
    try:
        for sec in soup.findAll("div",{"class":"tooltip-container"}):
            e = sec.find("span")
            #print(e)
            i = str(e.renderContents().strip())
            q = i.replace("\\n","").replace(" ","").encode('utf-8')
            print("Rating = {}".format(str(q)[4:len(q)+1])) 
            k = "Rating"
            v = str(str(q)[4:len(q)+1])
            if v != "":
                writeInJSONFormat(k,v)  
    except:
        print("No Rating")
            
    try:
        for sec in soup.findAll("li", {"class":"list-item"}):
            b = str(sec.findChildren()[0].renderContents().strip()).encode('utf-8')
            c = str(sec.findChildren()[1].renderContents().strip()).encode('utf-8')    
            if 'span' not in c:
                print("{} = {}".format(str(b)[4:len(b)+1],str(c)[4:len(c)+1]))
                try:
                    k = str(str(b)[4:len(b)+1])
                    v = str(str(c)[4:len(c)+1])
                    if v != "":
                        writeInJSONFormat(k,v)
                except:
                    print("Not available")
    except:
        print("Not Available")

# Combine all the key value pairs to make a complete JSON
def makeJSON():
    jsonLine = "{"
    for eachPair in jsonList:
        if jsonLine == "{":
            jsonLine += eachPair
        else:
            jsonLine += "," + eachPair
    
    jsonLine += "}" 
    return jsonLine 

# Iterate through all the files in a folder
def iterateThroughAllFiles():
    fileOut = open("extractionsUpdated1.json","w")
    for baseFolder, folderNames, nameOfFiles in os.walk("\\XXXXXXXXXXX\\data"):
        for textFileName in fnmatch.filter(nameOfFiles, '*.txt'):
            textFilePath = baseFolder + '\\' + os.path.join(textFileName)
            openFile(textFilePath)
            process()
            if len(jsonList) >= 2:
                js = makeJSON()
                print(js)
                fileOut.write(js + "\n")
    fileOut.close()

# Initiate the process
iterateThroughAllFiles()
     