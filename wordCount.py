#!/urs/bin/env python3

import sys    # command line arguments
import re     # Regular expression tools
import os     #check if files exist

#check for format
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output text file>" )
    exit()

textFName = sys.argv[1] #input text file
outFName = sys.argv[2]  #output text file

#first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()

# check that text files exist
if not os.path.exists(textFName):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()
#master dictionary
master  = {}

#open the file
with open(textFName,"r") as inputFile:
    for line in inputFile:                 
        wordSplice = re.split(r'\W+',line)
        for  word  in  wordSplice:
            word =  word.lower() #lowercase
            if word not  in master.keys():
                 master[word] = 1       #add word
            else:
                master[word] += 1       #increase value
del master[""]
inputFile.close()

#write to the file
with open(outFName,'w') as outputFile:
    for x ,y in sorted(master.items()):  
        outputFile.write( "%s %d\n" % (x , y) )
outputFile.close()
print("Words counted successfully")
