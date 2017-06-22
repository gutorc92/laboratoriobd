#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys

def main():
    if len(sys.argv) < 3:
        print("Precisa de um arquivo")
        return None
    file_name = sys.argv[1]
    encoding = sys.argv[2]
    print(file_name)
    fn = open(file_name, 'r', encoding=encoding)
    text = fn.read()
    soup = BeautifulSoup(text, 'html.parser')
    ps = soup.find_all('p')
    for p in ps:
        #print(type(p), p)
        t = p.text
        if t:
            t = str(t)
            #print("Linha: ", t)
            t = t.replace("\n", " ")
            m = re.search('(Art\.\s+\d+\w{1})\s+-*(.*)', t) 
            if(m is not None):
                arg_pass = m.group(1)
                print("Artigo:", m.group(1))
                print("Texto:", m.group(2))
                #print("Achou",t)           
            m = re.search('(§ \d+)º\s+-\s+(.*)',t)
            if(m is not None):
                print("Paragrafo:", m.group(1))  
                print("texto:",  m.group(2))  
            m = re.search('(I|II)\s+\u2013\s+(.*)',t)
            if(m is not None):
                print("Alinea:", m.group(1))  
                print("texto:",  m.group(2)) 


if __name__ == "__main__":
    main()
