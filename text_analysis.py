#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests as req
import os
import codecs
from settings import Settings
import logging
from datetime import datetime
import textmining

        
def read_law(settings):
    tdm = textmining.TermDocumentMatrix()
    files_list = [x for x in os.listdir(settings.join("leis")) if os.path.isfile(settings.join("leis", x))]
    for file_path in files_list:
        with codecs.open(settings.join("leis", file_path), "r", "utf-8") as handle:
            tdm.add_doc(handle.read())

    tdm.write_csv("matrix.csv", cutoff=1)


if __name__ == "__main__":
    s = Settings()
    s.extract_settings()
    read_law(s)
