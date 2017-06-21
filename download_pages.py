#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests as req
import os

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
        

def main():
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


if __name__ == "__main__":
    main()
