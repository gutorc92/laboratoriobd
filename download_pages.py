#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests as req
import os
import codecs
from settings import Settings
import logging
from datetime import datetime

def generate_dic_leis():
    years = {"2017": {"begin" : 13414, "end": 13507, "period": "2015-2018"},
             "2016": {"begin": 13243, "end": 13413, "period": "2015-2018"},
             "2015": {"begin": 13080, "end": 13242, "period": "2015-2018"},
             "2014": {"begin": 12952, "end": 13079, "period": "2011-2014"},
             "2013": {"begin": 12780, "end": 12951, "period": "2011-2014"},
             "2012": {"begin": 12587, "end": 12779, "period": "2011-2014"},
             "2011": {"begin": 12379, "end": 12586, "period": "2011-2014"},
             "2010": {"begin": 12188, "end": 12378, "period": "2007-2010"},
             "2009": {"begin": 11898, "end": 12187, "period": "2007-2010"},
             "2008": {"begin": 11639, "end": 11897, "period": "2007-2010"},
             "2007": {"begin": 11441, "end": 11638, "period": "2007-2010"},
             "2006": {"begin": 11263, "end": 11440, "period": "2004-2016"},
             "2005": {"begin": 11087, "end": 11262, "period": "2004-2016"},
             "2004": {"begin": 10835, "end": 11086, "period": "2004-2016"},
             "2003": {"begin": 10638, "end": 10834, "period": ""},
             "2002": {"begin": 10401, "end": 10637, "period": ""},
             "2001": {"begin": 10171, "end": 10400, "period": ""},
             "2000": {"begin": 9953, "end": 10170, "period": ""},
             "1999": {"begin": 9778, "end": 9952, "period": ""},
             "1998": {"begin": 9600, "end": 9777, "period": ""},
             "1997": {"begin": 9431, "end": 9599, "period": ""},
             "1996": {"begin": 9254, "end": 9430, "period": ""},
             "1995": {"begin": 8973, "end": 9253, "period": ""},
             "1994": {"begin": 8842, "end": 8972, "period": ""},
             "1993": {"begin": 8617, "end": 8841, "period": ""},
             "1992": {"begin": 8395, "end": 8616, "period": "1989_1994"},
             "1991": {"begin": 8157, "end": 8394, "period": "1989_1994"},
             "1990": {"begin": 7991, "end": 8156, "period": "1989_1994"},
             "1989": {"begin": 7715, "end": 7990, "period": "1989_1994"},
             "1988": {"begin": 7647, "end": 7714, "period": "1980-1988"},
             "1987": {"begin": 6896, "end": 7646, "period": "1980-1988"}}
    return years

def generate_link():
    urls = []
    years = generate_dic_leis()
    for year in years:
        for i in range(years[year]["begin"], years[year]["end"] + 1 ):
            year_n = int(year)
            if year_n >= 2006 and year_n <= 2017:
                url = "http://www.planalto.gov.br/ccivil_03/_ato{periodo}/{ano}/lei/L{lei}.htm"  # 2007  a 2017
                urls.append(url.format(periodo=years[year]["period"], ano=year, lei=i))
            if year_n >= 2004 and year_n <= 2016:
                url = "http://www.planalto.gov.br/ccivil_03/_Ato{periodo}/{ano}/Lei/L{lei}.htm"  # 2004 a 2006
                urls.append(url.format(periodo=years[year]["period"], ano=year, lei=i))
            if year_n >= 2002 and year_n <= 2013:
                url = "http://www.planalto.gov.br/ccivil_03/Leis/{ano}/L{lei}.htm"  # 2002 a 2003
                urls.append(url.format(ano=year, lei=i))
            if year_n == 2001:
                url = "http://www.planalto.gov.br/ccivil_03/Leis/LEIS_{ano}/L{lei}.htm"  # 2001
                urls.append(url.format(ano=year, lei=i))
            if year_n >= 1993 and year_n <= 2000:
                url = "http://www.planalto.gov.br/ccivil_03/Leis/L{lei}.htm"  # 1993 a 2000
                urls.append(url.format(lei=i))
            if year_n >= 1981 and year_n <= 1992:
                url = "http://www.planalto.gov.br/ccivil_03/Leis/{periodo}/l{lei}.htm"  # 1981 a 1992
                urls.append(url.format(periodo = years[year]["period"], lei=i))
    
    return urls
        
def save_law(file_path, text):
    with codecs.open(file_path, "w", "utf-8") as handle:
        handle.write(text)

def create_log_(id, settings):
    log_file = "log_extract_numbers_" + str(id) + "_" + datetime.now().strftime("%d_%m_%Y_%H_%M")
    log_file = os.path.join(settings.path, "log", log_file)
    print("log file", log_file)
    logging.basicConfig(filename=log_file, format='%(levelname)s:%(message)s', level=logging.INFO)

def main():
    s = Settings()
    s.extract_settings()
    create_log_(2, s)
    #urls = ["http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/L13507.htm", "http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/L13506.htm"]
    urls = generate_link()
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
    dir_leis = os.path.join(s.path, "leis")
    if not os.path.exists(dir_leis):
        print("Diretorio não existe")
        return None
    session = req.Session()
    for url in urls:
        try:
            print("Lei found", url)
            t = session.get(url, headers=headers, timeout=0.1)
            t.raise_for_status()
            if t.status_code == req.codes.ok:
                filename = os.path.join(dir_leis,url.rsplit('/', 1)[-1])
                page = BeautifulSoup(t.content, "html.parser")
                div = page.find("body")
                save_law(os.path.join(s.path, filename), div.text )
        except:
            print("Lei not found", url)
            logging.exception("Exception ocorrur")


if __name__ == "__main__":
    main()
