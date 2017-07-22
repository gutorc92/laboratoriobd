#!/usr/bin/python3.4
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
from myPyArango import saveDocument, createRelacao

file_name = "leis/L13413.html"
#file_name = './DEL2848compilado.html'
fn = open(file_name, 'r', encoding="iso-8859-1")
text = fn.read()
soup = BeautifulSoup(text, 'html.parser')
ps = soup.find_all(text = True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True
visable_texts = filter(visible, ps)
handle = open("resultado.txt", "wb")

i = 0
for p in visable_texts:
    if p.find("Art") == -1 and p.find("§") == -1:
        p = p.replace("\n", "")
    if p:
        print(i, " ", p, len(p))
        i = i + 1

    if p:
        handle.write(bytes(p, "utf-8"))
handle.close()
