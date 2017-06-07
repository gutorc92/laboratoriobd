from pyArango.connection import *
import pyArango.collection as COL
from pyArango.collection import Collection, Field, Edges
import pyArango.validation as VAL
from pyArango.graph import Graph, EdgeDefinition

class Leis(COL.Collection):
    _validation = {
        'on_save': True,
        'on_set': False,
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


def main():
   print("Passou aqui")
   conn = Connection(username="root", password="teste")
   db = conn["legislacao"]
   db.createCollection("Leis")
   db.createCollection("Relacao")
   db.createGraph("TipoRelacao")

if __name__ == "__main__" :
    main() 
