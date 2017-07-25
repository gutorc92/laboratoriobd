#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests as req
import os
import time
import codecs
from selenium import webdriver

def get_main_dir():
    repositorio_dir = os.path.dirname(os.path.realpath(__file__))
    return(repositorio_dir)

def leis_dir():
    rep = get_main_dir()
    return(os.path.join(rep, "leis"))

def leis_artigos_corretos():
    rep = get_main_dir()
    return(os.path.join(rep, "leis_artigos_corretos"))

def resultados_dir():
    rep = get_main_dir()
    return(os.path.join(rep, "resultados"))

def files_diretorio(dir_input):
    onlyfiles = [f for f in os.listdir(dir_input) if os.path.isfile(os.path.join(dir_input, f))]
    print(onlyfiles)
    return(onlyfiles)

def files_diretorio_real_path(dir_input):
    onlyfiles = [os.path.join(dir_input,f) for f in os.listdir(dir_input) if os.path.isfile(os.path.join(dir_input, f))]
    print(onlyfiles)
    return(onlyfiles)

def real_path_arquivos(dir_path, file_name):
    return(os.path.join(dir_path, file_name))

def remove_file(name):
    if os.path.isfile(name):
        os.remove(name)

def main():
    files_diretorio_real_path(leis_artigos_corretos())
    #webdriver_download()

if __name__ == "__main__":
    main()
