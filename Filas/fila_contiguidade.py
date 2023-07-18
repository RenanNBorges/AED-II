"""
Feito por Renan Nunes Borges

Arquivo contendo representações de Tipos Abstratos de Dados Fila

Filas usam do príncipio de FIFO (First in, First Out)
Tem acesso restrito há o primeiro e ultimo elemento que foi inserido
Mas as operações de consulta e exclusão são somente pelo primeiro
OPERAÇÕES que são afetas pelas restrições:
 * Inserir
 * Excluir
 * Consultar

--------------------- OPERAÇÕES ---------------------
• criar uma fila vazia
• inserir um nó no final da fila
• excluir o nó do início da fila
• consultar nó do início da fila
• destruir a fila

Filas de contiguidade física tem as seguintes propriedades:
LI : limite inferior da área
ini : início da fila
fim : final da fila
LS : limite superior da área
"""


class StaticQueue:
    def __init__(self, size):
        self.li = 0
        self.ls = size - 1
        self.vector = [None] * size
        self.ini = -1
        self.end = -1


    def is_empty(self):
        if self.ini and self.end == -1:
            return True
        else:
            return False

    def peek(self):
        if not (self.is_empty()):
            return self.vector[self.ini]
        else:
            return None

    def insert(self, data):
        # Testar se tem espaço
        if (self.ini == self.li and self.end == self.ls) or (self.end == self.ini - 1):
            return False

        else:
            # Inserir no Inicio
            if self.is_empty():
                self.ini = 0
                self.end = self.ini

            elif self.end == self.ls and self.ini:
                self.end = self.li

            # Inserir no meio e no fim
            else:
                self.end = self.end + 1

            self.vector[self.end] = data
            return True

    def remove(self):
        if not (self.is_empty()):
            if self.ini == self.end:
                self.vector[self.ini] = None

                self.ini = -1
                self.end = -1

            elif self.ini == self.ls and (self.li <= self.end < self.ini):
                self.vector[self.ls] = None
                self.ini = self.li

            else:
                self.ini = self.ini + 1
                self.vector[self.ini-1] = None

            return True
        else:
            return False

    def destroy(self):
        while (self.ini and self.end) != -1:
            self.remove()


queue_teste = StaticQueue(3)
queue_teste.insert(1)
queue_teste.insert(2)
queue_teste.insert(3)
queue_teste.insert(4)
queue_teste.insert(5)
queue_teste.remove()
queue_teste.insert(5)
queue_teste.remove()
queue_teste.insert(6)
queue_teste.remove()
queue_teste.remove()
queue_teste.insert(7)
queue_teste.insert(8)
queue_teste.insert(9)
queue_teste.peek()
queue_teste.destroy()
queue_teste.peek()
