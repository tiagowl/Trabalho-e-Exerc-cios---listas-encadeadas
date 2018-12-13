#! usr/bin/python3

class Pilha(object):
    def __init__(self):
        self.dados = []

    def append(self, dado):
        self.dados.append(dado)

    def pop(self):
        return self.dados.pop(-1)

    def isEmpty(self):
        len(self.dados) == 0
