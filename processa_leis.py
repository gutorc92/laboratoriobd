#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
from utils import *
import filecmp
from get_artigos import separar_leis

def outra():
    if len(sys.argv) < 3:
        print("Precisa de um arquivo")
        return None
    file_name = sys.argv[1]
    encoding = sys.argv[2]
    output_file = sys.argv[3]
    print(file_name)
    text = read_input(file_name, encoding)
    if output_file:
        fn1 = open_output(file_name, encoding)
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
            
def verificar_output(correto, gerado):
    if not filecmp.cmp(correto, gerado):
        print("Files not correct: ", correto, gerado)


def main():
   leis_convertidas = files_diretorio(leis_artigos_corretos())
   for lei in leis_convertidas:
        filename, file_extension = os.path.splitext(lei)
        html_file = real_path_arquivos(leis_dir(), filename + ".htm")
        output_file = real_path_arquivos(resultados_dir(), filename + ".txt")
        remove_file(output_file)
        correct_file = real_path_arquivos(leis_artigos_corretos(), lei)
        if os.path.isfile(html_file):
            print(correct_file, html_file, output_file)
            separar_leis(html_file, "utf-8", output_file)
            verificar_output(correct_file, output_file)

 
if __name__ == "__main__":
    main()
