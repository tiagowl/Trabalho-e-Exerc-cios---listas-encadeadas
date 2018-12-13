#! usr/bin/python3

class Fila(object):
    def __init__(self, dados):
        self.dados = []

    def append(self, dado):
        self.dados.append(dado)

    def pop(self):
        return self.dados.pop(-1)

    def isEmpty(self):
        len(self.dados) == 0
