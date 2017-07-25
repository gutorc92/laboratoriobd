#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Precisa de um arquivo")
        return None
    file_name = sys.argv[1]
    encoding = sys.argv[2]
    output_file = sys.argv[3]
    print(file_name)
    text = read_input(file_name, encoding)
    fn1 = open_output(file_name, "utf-8")
    soup = BeautifulSoup(text, 'html.parser')
    ps = soup.find_all('p')
    print("Quantos ps foram encontrados: ", len(ps))
    for p in ps:
        #print(type(p), p)
        t = p.text
        if t:
            t = str(t)
            t = t.strip()
            t = t.encode("utf-8").decode("utf-8")
            fn1.write(t)
    fn1.close()
            
def read_input(file_name, encoding):
    fn = open(file_name, 'r', encoding=encoding)
    text = fn.read()
    fn.close()
    return text

def open_output(file_name, encoding):
    file_name = os.path.join("convertidos", os.path.basename(file_name))
    print(file_name)
    fn = open(file_name, 'w', encoding=encoding)
    return fn

if __name__ == "__main__":
    main()
