from pyArango.connection import *
import pyArango.collection as COL
from pyArango.collection import Collection, Field, Edges
import pyArango.validation as VAL
from pyArango.graph import Graph, EdgeDefinition

class Leis(COL.Collection):
    _validation = {
        'on_save': True,
        'on_set': True,
        'allow_foreign_fields': True
    }
    _fields = {
        'texto' : Field(validators = [VAL.NotNull()]),
        'identificador' : Field()
    }

class Relacao(Edges):
    _fields = {
        "tipo" : Field()
    }

class TipoRelacao(Graph):
    _edgeDefinitions = (EdgeDefinition("Relacao", fromCollections = ["Leis"], toCollections = ["Leis"]), )
    _orphanedColletions = []


def getdb():
    conn = Connection(username="root", password="testando")
    if not conn.hasDatabase("legislacao"):
        conn.createDatabase(name = "legislacao")
    db = conn["legislacao"]
    return db

def getLeis():
    db = getdb()
    if db.hasCollection("Leis"):
        return db["Leis"]
    return None

def saveDocument(texto, identificador):
    i = getLeis()
    q = i.createDocument()
    q["identificador"] = identificador
    q["texto"] = texto
    q.save()

def main():
   db = getdb()
   db.createCollection("Leis")
   db.createCollection("Relacao")
   db.createGraph("TipoRelacao")

if __name__ == "__main__" :
    main() 
