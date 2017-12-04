# -*- coding: utf-8 -*-
import os
import logging
import codecs
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
from settings import Settings
from datetime import datetime


class ReadSentences(object):

    def __init__(self):
        self.s = Settings()
        self.s.extract_settings()
        self.createLog()

    def createLog(self):
        log_file = "log" + datetime.now().strftime("%d%m%Y_%M_%H")
        self.log_file = os.path.join(self.s.path, "log", log_file)
        logging.basicConfig(filename=self.log_file, format='%(levelname)s:%(message)s', level=logging.INFO)

    def getJudge(self, text):
        judge = ""
        pattern = re.compile(r"Este documento é cópia do original, assinado digitalmente por ([A-Z ]*), liberado nos autos em", re.MULTILINE)
        for match in pattern.finditer(text):
            match_return = match.groups()
            print(match_return[0])
            judge = match_return[0]
        return judge

    def readText(self):
        text = ""
        with codecs.open(os.path.join(self.s.path, "leis", "l6896.htm"), "r", "UTF-8") as handle:
           for line in handle.readlines():
               line = line.rstrip().lower()
               text += " " + line
        line = re.sub("\s+", " ", text)
        return text

    def tokenizer(self):
        # portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
        tokens = nltk.word_tokenize(self.readText())
        print(len(tokens))
        # nltk_text = nltk.Text(tokens)
        # print(type(nltk_text))
        fd1 = nltk.FreqDist(tokens)
        for f in fd1:
            print(f, fd1[f])

    def read(self):
        portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
        newcorpus = PlaintextCorpusReader(os.path.join(self.s.path, "leis"), ".*", sent_tokenizer=portuguese_sent_tokenizer)
        ponctuation = [".","!","-","?",",","lei","artigo",")","(","subchefia",":","presidente","$"]
        #print(newcorpus.words())
        for files in newcorpus.fileids():
            words = newcorpus.words(files)
            words = [w.lower() for w in words]
            filtered_words = [word for word in words if word not in stopwords.words("portuguese")]
            filtered_words = [word for word in filtered_words if word not in ponctuation]
            fd1 = nltk.FreqDist(filtered_words)
            print(files, fd1.most_common(10))


if __name__ == "__main__":
    r = ReadSentences()
    r.read()
    #print(stopwords.words("portuguese"))

