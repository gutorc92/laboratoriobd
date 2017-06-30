#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
from myPyArango import saveDocument, createRelacao

def readText(filename):
    f = open(filename, "r")
    t = f.read()
    return t

def findArt(t):
    m = re.search('(Art\. \d+)\s+-\s+(.*)', t) 
    if(m is not None):
        arg_pass = m.group(1)
        print(m.group(1))
        print(m.group(2))
        #print("Achou",t)           
    
if __name__ == "__main__":
    t = readText("resultado.txt")
    print(t)
    findArt(t)
