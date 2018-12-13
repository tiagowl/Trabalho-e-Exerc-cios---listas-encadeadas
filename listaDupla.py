#! usr/bin/python3

from no import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, dado):
        no = No(dado)

        if self.tail == None:
            self.head = no
        else:
            self.tail = no.anterior

        self.tail = no
        no.indice += 1


    def addFirst(self, dado):
        no = No(dado)

        if self.head == None:
            self.tail = no
        else:
            no.proximo = self.head
            self.head.anterior = no

        self.head = no
        no.indice += 1
