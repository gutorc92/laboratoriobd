#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re

fn = open('./DEL2848compilado.html', 'r')
text = fn.read()
soup = BeautifulSoup(text, 'html.parser')
ps = soup.find_all('p')
for p in ps:
    t = p.string
    if type(t) is NavigableString:
        t = str(t)
        t = t.replace("\n", " ")
        #print("Linha: ", t)
        m = re.search('(Art\. \d+)\s+-\s+(.*)', t) 
        if(m is not None):
            arg_pass = m.group(1)
            #print(m.group(1))
            #print(m.group(2))
            #print("Achou",t)           
        m = re.search('(§ \d+)º\s+-\s+(.*)',t)
        if(m is not None):
            print(m.group(1))  
            print(m.group(2))  
