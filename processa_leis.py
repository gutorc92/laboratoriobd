#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
from utils import *
import filecmp
from get_artigos import separar_leis, get_charset

            
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
            separar_leis(html_file, get_charset(html_file), output_file)
            verificar_output(correct_file, output_file)

 
if __name__ == "__main__":
    main()
