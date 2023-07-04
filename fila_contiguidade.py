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
        self.__li = 0
        self.__ls = size - 1
        self.__vector = [None] * size
        self.__ini = -1
        self.__end = -1

    def is_empty(self):
        if self.__ini and self.__end != -1:
            return False
        else:
            return True

    def peek(self):
        if not(self.is_empty()):
            return print(self.__vector[self.__vector])
        else:
            return print(None)

    def insert(self, data):
        # Testar se tem espaço
        if (self.__ini == self.__li and self.__end == self.__ls) or (self.__end == self.__ini - 1):
            return False

        else:
            # Inserir no Inicio
            if self.__end == self.__ls:
                self.__end = self.__li

            # Inserir no meio e no fim
            else:
                self.__end = self.__end + 1

            self.__vector[self.__end] = data
            return True

    def remove(self):
        if self.__ini < self.__end:
            self.__ini = self.__ini + 1
        elif self.__ini == self.__ls and self.__li == self.__end:
            self.__ini = self.__li

    def destroy(self):
        self.__ini = -1
        self.__end = -1


queue_teste = StaticQueue(13)
queue_teste.peek()
