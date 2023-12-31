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

Filas encadeadas tem as seguintes propriedades:
Um descritor com o n[o de inicio e fim
Não há limite em uma fila encadeada
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} <- {self.next}'


class DynamicQueue:
    def __init__(self):
        self.ini = None
        self.end = None

    def __repr__(self):
        return f'{self.ini}'

    def is_empty(self):
        if self.ini and self.end is not None:
            return False
        else:
            return True

    def insert(self, data):
        new_element = Node(data)
        if self.is_empty():
            self.ini = new_element

        else:
            self.end.next = new_element

        self.end = new_element

    def peek(self):
        if not(self.is_empty()):
            return self.ini.data
        else:
            return None

    def remove(self):
        if self.is_empty():
            return False
        else:
            if self.ini != self.end:
                self.ini = self.ini.next
            else:
                self.ini = None
                self.end = None
            return True

    def destroy(self):
        self.ini = None
        self.end = None

