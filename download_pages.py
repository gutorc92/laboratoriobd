#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests as req
import os
import time
import codecs
from selenium import webdriver

def generate_link():
    urls = []
    periodos = ["2011-2014", "2015-2018"]
    url = "http://www.planalto.gov.br/ccivil_03/_ato{periodo}/{ano}/lei/L{lei}.htm"
    for p in periodos:
        years = p.split( "-")
        for year in range(int(years[0]), int(years[1]) + 1): 
            for i in range(12379, 13452):
                urls.append(url.format(periodo = p, ano = year, lei=i))
    
    return urls

def save_urls():
    urls = generate_link()
    repositorio_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(repositorio_dir, "urls")
    file_object = codecs.open(file_name, "w","utf-8")
    for url in urls:
        file_object.write(url+"\n")
    file_object.close()


def old_way():
    urls = generate_link()
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
    dir_leis = os.path.join(os.path.abspath("."), "leis")
    if not os.path.exists(dir_leis):
        print("Diretorio não existe")
        return None
    for url in urls:
        try:
            print("Lei found", url)
            t = req.get(url, headers=headers, timeout=0.1)
            t.raise_for_status()
            filename = os.path.join(dir_leis,url.rsplit('/', 1)[-1])
            print("Filename", filename)
            with open(filename, 'wb') as handle:
                for block in t.iter_content(1024):
                    handle.write(block)
        except:
            print("Lei not found", url)

def save_file(html, nome_number):
    leis_dir = os.path.dirname(os.path.realpath(__file__))
    leis_dir = os.path.join(leis_dir, "leis")
    file_name = os.path.join(leis_dir, nome_number)
    file_object = codecs.open(file_name, "w","utf-8")
    file_object.write(html)
    file_object.close()

def get_urls():
    urls_todas = generate_link()
    url_verdadeiras = []
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
    print("Comecando")
    for url in urls_todas:
        try:
            #print(os.path.basename(url))
            request = req.get(url, headers=headers, timeout=3)
            if request.status_code == 200:
                url_verdadeiras.append(url)
                print('Web site exists ', url)
            else:
                print('Web site does not exist') 
        except KeyboardInterrupt:
            break;
        except:
                print('Web site does not exist ', url) 

    return(url_verdadeiras)

def check_lei_already_downloaded(name):
    leis_dir = os.path.dirname(os.path.realpath(__file__))
    leis_dir = os.path.join(leis_dir, "leis")
    file_name = os.path.join(leis_dir,name)
    return os.path.isfile(file_name)


def webdriver_download():
    chrome_dir = os.path.dirname(os.path.realpath(__file__))
    chrome_path = os.path.join(chrome_dir, "chromedriver", "chromedriver")
    print(chrome_path,chrome_dir, os.path.realpath(__file__))
    urls_verdadeiras = get_urls()
    driver = webdriver.Chrome(chrome_path)
    for url in urls_verdadeiras:
        try:
            base_name = os.path.basename(url)
            if not check_lei_already_downloaded(base_name):
                driver.get(url)
                driver.implicitly_wait(10)
                save_file(driver.page_source, base_name)
                time.sleep(5)
        except KeyboardInterrupt:
            break;
        except:
            print("Url was not found ", url)
    driver.quit()

def main():
    save_urls()
    #webdriver_download()

if __name__ == "__main__":
    main()
