#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
def main():
    pass

def separar_leis(file_name, encoding, output_file):
    text = read_input(file_name, encoding)
    if output_file :
        fn1 = open(output_file, "w", encoding=encoding)
    soup = BeautifulSoup(text, 'html.parser')
    ps = soup.find_all('p')
    print("Quantos ps foram encontrados: ", len(ps))
    for p in ps:
        #print(type(p), p)
        t = p.text
        if t:
            t = str(t)
            t = t.strip()
            t = t.replace("\n", " ")
            r = find_artigo(t, fn1)           
            if r is None:
                print(t)
    if output_file:
        fn1.close()
            
def read_input(file_name, encoding):
    fn = open(file_name, 'r', encoding=encoding)
    text = fn.read()
    fn.close()
    return text

def open_output(file_name, encoding):
    file_name = os.path.join("resultados", os.path.basename(file_name))
    print(file_name)
    fn = open(file_name, 'w', encoding=encoding)
    return fn

def find_artigo(text, fn = None):
    m = re.search('^(Art.*\s+\d+(\u00B0|\.|o||º))\s+-*(.*)', text) 
    if(m is not None):
        if fn is None:
            print("Artigo:", m.group(1), fn)
            print("Texto:", m.group(3), fn)
            #print("Achou",t)
        else:
            fn.write("Artigo: " + m.group(1) + "\n")
            fn.write("Texto: " + m.group(3).replace("  "," ") + "\n")
    else:
        print("Nao achou artigo")
        return None
    return 1

def find_paragrafo(text):
    m = re.search('(§ \d+)º\s+-\s+(.*)',text)
    if(m is not None):
        print("Paragrafo:", m.group(1))
        print("Texto:", m.group(2))
        #print("Achou",t) 
    else:
        print("Nao achou paragrafo")
        return None
    return 1

def find_alinea(text):
    m = re.search('(I|II)\s+\u2013\s+(.*)',text)
    if(m is not None):
        print("Alinea:", m.group(1))  
        print("texto:",  m.group(2))
    else:
        print("Nao achou alinea")
        return None
    return 1

if __name__ == "__main__":
    main()
